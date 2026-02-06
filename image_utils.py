"""
Image dimension utilities without third-party dependencies.

GitHub strips inline CSS styles from README images for security, so we can't use
max-width. Instead, we fetch image headers to check dimensions and only add a
width attribute when the image exceeds our max size - keeping small images at
their natural size.
"""

import struct
from urllib.request import Request, urlopen


def get_image_width(url: str) -> int | None:
    """Fetch image from URL and return its width by parsing headers."""
    try:
        request = Request(url, headers={"User-Agent": "Talon-Readme-Generator"})
        with urlopen(request, timeout=10) as response:
            data = response.read(1024)  # First 1KB is enough for headers

            # PNG: width at bytes 16-20
            if data[:8] == b'\x89PNG\r\n\x1a\n':
                width = struct.unpack('>I', data[16:20])[0]
                return width

            # GIF: width at bytes 6-8 (little-endian)
            if data[:6] in (b'GIF87a', b'GIF89a'):
                width = struct.unpack('<H', data[6:8])[0]
                return width

            # JPEG: need to find SOF marker
            if data[:2] == b'\xff\xd8':
                i = 2
                while i < len(data) - 9:
                    if data[i] != 0xff:
                        i += 1
                        continue
                    marker = data[i + 1]
                    # SOF markers (0xC0-0xCF except 0xC4, 0xC8, 0xCC)
                    if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                                  0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                        width = struct.unpack('>H', data[i + 7:i + 9])[0]
                        return width
                    # Skip this segment
                    length = struct.unpack('>H', data[i + 2:i + 4])[0]
                    i += 2 + length

            return None
    except Exception as e:
        print(f"Warning: Could not get image dimensions from {url}: {e}")
        return None
