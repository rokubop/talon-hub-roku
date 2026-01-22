# Talon Hub Roku

A collection of my Talon repos for UI, mouse control, input mapping, parrot, and gaming you may find useful.

This is auto-generated from repo manifests.

## Repos

| Name | Description |
|------|-------------|
| <nobr>**[talon-ui-elements](#talon-ui-elements)**</nobr> | Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon. |
| <nobr>**[talon-manifest-generator](#talon-manifest-generator)**</nobr> | Scripts for generating package-like files for your Talon repo such as manifest.json and _version.py with automatic detection for contributions and dependencies |
| <nobr>**[talon-parrot-tester](#talon-parrot-tester)**</nobr> | Visual tool for testing parrot integration with Talon |
| <nobr>**[talon-input-map](#talon-input-map)**</nobr> | This is an alternate way to define your input commands in a way that supports combos, throttling, debounce, switching out configs easily without needing to create new modes. Works with parrot noises, foot pedals, face tracking, or any other input source. |
| <nobr>**[talon-parrot-rig](#talon-parrot-rig)**</nobr> | Add a description of your Talon package here. |
| <nobr>**[talon-mouse-rig](#talon-mouse-rig)**</nobr> | Control your mouse with position, speed, direction, and vector commands, over time and with advanced behaviors |
| <nobr>**[talon-pynput-slot](#talon-pynput-slot)**</nobr> | Uses pynput to listen to key events mapped to slots 1-4 (each has a Talon ctx action), preventing unwanted repeats or releases when pressing other keys during voice commands. Useful for foot pedals or keys + voice commands at the same time. |
| <nobr>**[talon-face-tester](#talon-face-tester)**</nobr> | Add a description of your Talon package here. |
| <nobr>**[talon-obs-integration](#talon-obs-integration)**</nobr> | Integrate Talon with OBS Studio for controlling streaming/recording/scenes/sources. |

---

## Repo Details


### talon-ui-elements

🔗 **GitHub:** [rokubop/talon-ui-elements](https://github.com/rokubop/talon-ui-elements)

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-reference-blue)
![License](https://img.shields.io/badge/license-Unlicense-green)

![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-ui-elements?style=social)

Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon.

<img src="https://raw.githubusercontent.com/rokubop/talon-ui-elements/main/examples/ui_elements_preview.png" width="400">

| | |
|---|---|
| **Namespace** | `user.ui_elements` |
| **Tags** | ui |
| **License** | MIT |
| **Contributes** | 31 actions, 7 settings, 1 tags, 1 captures |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.ui_elements`
- `user.ui_elements_debug_gc`
- `user.ui_elements_dev_tools`
- `user.ui_elements_examples`
- `user.ui_elements_get_input_value`
- `user.ui_elements_get_node`
- `user.ui_elements_get_state`
- `user.ui_elements_get_trees`
- `user.ui_elements_hide`
- `user.ui_elements_hide_all`
- `user.ui_elements_highlight`
- `user.ui_elements_highlight_briefly`
- `user.ui_elements_hint_action`
- `user.ui_elements_is_active`
- `user.ui_elements_key_action`
- `user.ui_elements_register_effect`
- `user.ui_elements_reset_all_scale_overrides`
- `user.ui_elements_scale_decrease`
- `user.ui_elements_scale_increase`
- `user.ui_elements_scale_reset`
- `user.ui_elements_set_property`
- `user.ui_elements_set_state`
- `user.ui_elements_set_text`
- `user.ui_elements_show`
- `user.ui_elements_storybook_toggle`
- `user.ui_elements_svg`
- `user.ui_elements_test_runner`
- `user.ui_elements_toggle`
- `user.ui_elements_toggle_hints`
- `user.ui_elements_unhighlight`
- `user.ui_elements_version`

**Settings:**
- `user.ui_elements_hints_button_first_char`
- `user.ui_elements_hints_input_text_first_char`
- `user.ui_elements_hints_link_first_char`
- `user.ui_elements_hints_show`
- `user.ui_elements_hints_size`
- `user.ui_elements_scale`
- `user.ui_elements_scroll_speed`

**Tags:**
- `user.ui_elements_hints_active`

**Captures:**
- `user.ui_elements_hint_target`

</details>

---


### talon-manifest-generator

🔗 **GitHub:** [rokubop/talon-manifest-generator](https://github.com/rokubop/talon-manifest-generator)

![Version](https://img.shields.io/badge/version-2.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-manifest-generator?style=social)

Scripts for generating package-like files for your Talon repo such as manifest.json and _version.py with automatic detection for contributions and dependencies

| | |
|---|---|
| **License** | Unlicense |


---


### talon-parrot-tester

🔗 **GitHub:** [rokubop/talon-parrot-tester](https://github.com/rokubop/talon-parrot-tester)

![Version](https://img.shields.io/badge/version-0.7.0-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-parrot-tester?style=social)

Visual tool for testing parrot integration with Talon

<img src="https://raw.githubusercontent.com/rokubop/talon-parrot-tester/main/preview.png" width="400">

| | |
|---|---|
| **Namespace** | `user.parrot_tester` |
| **Tags** | parrot |
| **License** | MIT |
| **Dependencies** | talon-ui-elements `v0.13.0` |
| **Contributes** | 5 actions, 1 tags |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.parrot_tester_integration_ready`
- `user.parrot_tester_restore_parrot_integration`
- `user.parrot_tester_toggle`
- `user.parrot_tester_version`
- `user.parrot_tester_wrap_parrot_integration`

**Tags:**
- `user.parrot_tester`

</details>

---


### talon-input-map

🔗 **GitHub:** [rokubop/talon-input-map/](https://github.com/rokubop/talon-input-map/)

![Version](https://img.shields.io/badge/version-0.6.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-input-map/?style=social)

This is an alternate way to define your input commands in a way that supports combos, throttling, debounce, switching out configs easily without needing to create new modes. Works with parrot noises, foot pedals, face tracking, or any other input source.

| | |
|---|---|
| **Namespace** | `user.input_map` |
| **Tags** | parrot, noise, foot pedal, face |
| **Contributes** | 11 actions, 1 settings |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.input_map`
- `user.input_map_event_register`
- `user.input_map_event_unregister`
- `user.input_map_format_display`
- `user.input_map_format_display_dict`
- `user.input_map_handle`
- `user.input_map_mode_cycle`
- `user.input_map_mode_get`
- `user.input_map_mode_set`
- `user.input_map_tests`
- `user.input_map_version`

**Settings:**
- `user.input_map_combo_window`

</details>

---


### talon-parrot-rig

![Version](https://img.shields.io/badge/version-0.1.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange)

Add a description of your Talon package here.

| | |
|---|---|
| **Namespace** | `user.parrot_rig` |
| **Requires** | Eye Tracker, Parrot, Talon Beta |
| **Dependencies** | talon-input-map `v0.6.0`, talon-mouse-rig `v0.5.0`, talon-ui-elements `v0.13.0` |
| **Contributes** | 12 actions, 1 modes |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.parrot_rig_click`
- `user.parrot_rig_disable`
- `user.parrot_rig_enable`
- `user.parrot_rig_get_mode`
- `user.parrot_rig_get_state`
- `user.parrot_rig_reload`
- `user.parrot_rig_repeater`
- `user.parrot_rig_reverser`
- `user.parrot_rig_show_help`
- `user.parrot_rig_toggle`
- `user.parrot_rig_tracking_activate_full`
- `user.parrot_rig_version`

**Modes:**
- `user.parrot_rig`

</details>

---


### talon-mouse-rig

🔗 **GitHub:** [rokubop/talon-mouse-rig](https://github.com/rokubop/talon-mouse-rig)

![Version](https://img.shields.io/badge/version-0.5.0-blue) ![Status](https://img.shields.io/badge/status-prototype-red) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-mouse-rig?style=social)

Control your mouse with position, speed, direction, and vector commands, over time and with advanced behaviors

| | |
|---|---|
| **Namespace** | `user.mouse_rig` |
| **Tags** | mouse, movement |
| **License** | MIT |
| **Dev Dependencies** | talon-ui-elements `v0.13.0` |
| **Contributes** | 46 actions, 5 settings |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.mouse_rig`
- `user.mouse_rig_direction_by`
- `user.mouse_rig_direction_down`
- `user.mouse_rig_direction_left`
- `user.mouse_rig_direction_right`
- `user.mouse_rig_direction_to`
- `user.mouse_rig_direction_up`
- `user.mouse_rig_go_direction`
- `user.mouse_rig_go_down`
- `user.mouse_rig_go_left`
- `user.mouse_rig_go_right`
- `user.mouse_rig_go_up`
- `user.mouse_rig_pos_by`
- `user.mouse_rig_pos_by_value`
- `user.mouse_rig_pos_to`
- `user.mouse_rig_reload`
- `user.mouse_rig_reset`
- `user.mouse_rig_reverse`
- `user.mouse_rig_scroll_direction_by`
- `user.mouse_rig_scroll_direction_down`
- `user.mouse_rig_scroll_direction_left`
- `user.mouse_rig_scroll_direction_right`
- `user.mouse_rig_scroll_direction_to`
- `user.mouse_rig_scroll_direction_up`
- `user.mouse_rig_scroll_go_direction`
- `user.mouse_rig_scroll_go_down`
- `user.mouse_rig_scroll_go_left`
- `user.mouse_rig_scroll_go_right`
- `user.mouse_rig_scroll_go_up`
- `user.mouse_rig_scroll_increment_by`
- `user.mouse_rig_scroll_increment_to`
- `user.mouse_rig_scroll_speed_add`
- `user.mouse_rig_scroll_speed_to`
- `user.mouse_rig_speed_add`
- `user.mouse_rig_speed_mul`
- `user.mouse_rig_speed_to`
- `user.mouse_rig_state_direction`
- `user.mouse_rig_state_direction_cardinal`
- `user.mouse_rig_state_direction_x`
- `user.mouse_rig_state_direction_y`
- `user.mouse_rig_state_is_moving`
- `user.mouse_rig_state_pos`
- `user.mouse_rig_state_speed`
- `user.mouse_rig_stop`
- `user.mouse_rig_test_toggle_ui`
- `user.mouse_rig_version`

**Settings:**
- `user.mouse_rig_api`
- `user.mouse_rig_frame_interval`
- `user.mouse_rig_manual_movement_timeout_ms`
- `user.mouse_rig_pause_on_manual_movement`
- `user.mouse_rig_scale`

</details>

---


### talon-pynput-slot

🔗 **GitHub:** [rokubop/talon-pynput-slot](https://github.com/rokubop/talon-pynput-slot)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-pynput-slot?style=social)

Uses pynput to listen to key events mapped to slots 1-4 (each has a Talon ctx action), preventing unwanted repeats or releases when pressing other keys during voice commands. Useful for foot pedals or keys + voice commands at the same time.

| | |
|---|---|
| **Namespace** | `user.pynput_slot` |
| **Contributes** | 11 actions |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.pynput_slot_1_down`
- `user.pynput_slot_1_up`
- `user.pynput_slot_2_down`
- `user.pynput_slot_2_up`
- `user.pynput_slot_3_down`
- `user.pynput_slot_3_up`
- `user.pynput_slot_4_down`
- `user.pynput_slot_4_up`
- `user.pynput_slot_disable`
- `user.pynput_slot_enable`
- `user.pynput_slot_version`

</details>

---


### talon-face-tester

🔗 **GitHub:** [rokubop/talon-face-tester](https://github.com/rokubop/talon-face-tester)

![Version](https://img.shields.io/badge/version-0.1.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-face-tester?style=social)

Add a description of your Talon package here.

<img src="https://raw.githubusercontent.com/rokubop/talon-face-tester/main/preview.png" width="400">

| | |
|---|---|
| **Namespace** | `user.face_tester` |
| **Requires** | Talon Beta, Webcam |
| **Dependencies** | talon-ui-elements `v0.13.0` |
| **Contributes** | 4 actions, 3 tags |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.face_tester_record_gaze_xy`
- `user.face_tester_record_value`
- `user.face_tester_toggle`
- `user.face_tester_version`

**Tags:**
- `user.face_tester`
- `user.face_tester_activity`
- `user.face_tester_values`

</details>

---


### talon-obs-integration

![Version](https://img.shields.io/badge/version-0.1.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange)

Integrate Talon with OBS Studio for controlling streaming/recording/scenes/sources.

| | |
|---|---|
| **Namespace** | `user.obs` |
| **Contributes** | 23 actions |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.obs_connect`
- `user.obs_disconnect`
- `user.obs_get_current_scene`
- `user.obs_get_recording_status`
- `user.obs_get_scene_list`
- `user.obs_get_source_list`
- `user.obs_get_streaming_status`
- `user.obs_get_version`
- `user.obs_is_connected`
- `user.obs_scene_item_hide`
- `user.obs_scene_item_is_visible`
- `user.obs_scene_item_set_enabled`
- `user.obs_scene_item_show`
- `user.obs_scene_item_toggle`
- `user.obs_set_current_scene`
- `user.obs_set_scene_item_transform`
- `user.obs_start_recording`
- `user.obs_start_streaming`
- `user.obs_stop_recording`
- `user.obs_stop_streaming`
- `user.obs_toggle_recording`
- `user.obs_toggle_streaming`
- `user.obs_version`

</details>

---


---