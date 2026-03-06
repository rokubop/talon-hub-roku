# Talon Hub Roku

A collection of my Talon repos for UI, mouse control, input mapping, parrot, and eventually gaming.

Auto-generated from repo manifests.

## Repos

| Name | Description |
|------|-------------|
| **[talon&#8209;ui&#8209;elements](#talon-ui-elements)** | Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon. |
| **[talon&#8209;pack](#talon-pack)** | CLI tool for Talon repos. Catalogs contributions and dependencies, manages versioning, and generates README badges. |
| **[talon&#8209;parrot&#8209;tester](#talon-parrot-tester)** | Visual tool for testing parrot integration with Talon |
| **[talon&#8209;rig&#8209;core](#talon-rig-core)** | Shared core library for device rigs (mouse-rig, gamepad-rig). Provides base classes, lifecycle, layer groups, mode operations, and animation infrastructure. |
| **[talon&#8209;mouse&#8209;rig](#talon-mouse-rig)** | All purpose mouse rig for Talon with movement and scrolling. Prefers OS-specific relative movement to be compatible with games. |
| **[talon&#8209;gamepad&#8209;rig](#talon-gamepad-rig)** | All purpose gamepad rig with advanced stick manipulation and button handling, for Talon. |
| **[talon&#8209;input&#8209;map](#talon-input-map)** | This is an alternate way to define your input commands in a way that supports combos, throttling, debounce, switching out configs easily without needing to create new modes. Works with parrot noises, foot pedals, face tracking, or any other input source. |
| **[talon&#8209;noise&#8209;map](#talon-noise-map)** | Advanced remapping for your default Talon pop and hiss noises, using talon-input-map |
| **[talon&#8209;stable&#8209;input](#talon-stable-input)** | Bind keys or pedals to Talon actions that won't be interrupted by voice commands.  Uses pynput. |
| **[talon&#8209;parrot&#8209;rig](#talon-parrot-rig)** | A general-purpose 14-noise parrot mode for hands-free mouse control in Talon. |

---

## Repo Details


### talon-ui-elements

🔗 **GitHub:** [rokubop/talon-ui-elements](https://github.com/rokubop/talon-ui-elements)

![Version](https://img.shields.io/badge/version-0.15.0-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-ui-elements?style=social)

Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon.

<img src="https://raw.githubusercontent.com/rokubop/talon-ui-elements/main/examples/ui_elements_preview.png" width="450">

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


### talon-pack

🔗 **GitHub:** [rokubop/talon-pack](https://github.com/rokubop/talon-pack)

![Version](https://img.shields.io/badge/version-3.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-pack?style=social)

CLI tool for Talon repos. Catalogs contributions and dependencies, manages versioning, and generates README badges.

<img src="https://raw.githubusercontent.com/rokubop/talon-pack/main/preview.svg">

| | |
|---|---|
| **Tags** | package, manifest, version, badges |
| **License** | Unlicense |


---


### talon-parrot-tester

🔗 **GitHub:** [rokubop/talon-parrot-tester](https://github.com/rokubop/talon-parrot-tester)

![Version](https://img.shields.io/badge/version-0.8.1-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-parrot-tester?style=social)

Visual tool for testing parrot integration with Talon

<img src="https://raw.githubusercontent.com/rokubop/talon-parrot-tester/main/preview.png" width="450">

| | |
|---|---|
| **Namespace** | `user.parrot_tester` |
| **Tags** | parrot |
| **License** | MIT |
| **Dependencies** | [talon-ui-elements](#talon-ui-elements) `v0.14.0` |
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


### talon-rig-core

🔗 **GitHub:** [rokubop/talon-rig-core](https://github.com/rokubop/talon-rig-core)

![Version](https://img.shields.io/badge/version-0.5.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-rig-core?style=social)

Shared core library for device rigs (mouse-rig, gamepad-rig). Provides base classes, lifecycle, layer groups, mode operations, and animation infrastructure.

| | |
|---|---|
| **Namespace** | `user.rig_core` |
| **Tags** | rig |
| **License** | MIT |
| **Contributes** | 2 actions |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.rig_core`
- `user.rig_core_version`

</details>

---


### talon-mouse-rig

🔗 **GitHub:** [rokubop/talon-mouse-rig](https://github.com/rokubop/talon-mouse-rig)

![Version](https://img.shields.io/badge/version-4.1.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-mouse-rig?style=social)

All purpose mouse rig for Talon with movement and scrolling. Prefers OS-specific relative movement to be compatible with games.

<img src="https://raw.githubusercontent.com/rokubop/talon-mouse-rig/main/preview.svg">

| | |
|---|---|
| **Namespace** | `user.mouse_rig` |
| **Tags** | mouse, movement |
| **License** | MIT |
| **Dependencies** | [talon-rig-core](#talon-rig-core) `v0.5.0` |
| **Dev Dependencies** | [talon-ui-elements](#talon-ui-elements) `v0.14.0` |
| **Contributes** | 43 actions, 16 settings |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.mouse_rig`
- `user.mouse_rig_boost`
- `user.mouse_rig_boost_start`
- `user.mouse_rig_boost_stop`
- `user.mouse_rig_button_prime`
- `user.mouse_rig_move_continuous`
- `user.mouse_rig_move_continuous_smooth`
- `user.mouse_rig_move_delta`
- `user.mouse_rig_move_delta_smooth`
- `user.mouse_rig_move_reverse`
- `user.mouse_rig_move_rotate`
- `user.mouse_rig_move_stop`
- `user.mouse_rig_move_to`
- `user.mouse_rig_move_to_smooth`
- `user.mouse_rig_reload`
- `user.mouse_rig_reset`
- `user.mouse_rig_scroll_boost`
- `user.mouse_rig_scroll_boost_start`
- `user.mouse_rig_scroll_boost_stop`
- `user.mouse_rig_scroll_continuous`
- `user.mouse_rig_scroll_continuous_smooth`
- `user.mouse_rig_scroll_delta`
- `user.mouse_rig_scroll_delta_smooth`
- `user.mouse_rig_scroll_speed_add`
- `user.mouse_rig_scroll_speed_mul`
- `user.mouse_rig_scroll_speed_to`
- `user.mouse_rig_scroll_stop`
- `user.mouse_rig_sequence`
- `user.mouse_rig_speed_add`
- `user.mouse_rig_speed_mul`
- `user.mouse_rig_speed_to`
- `user.mouse_rig_state`
- `user.mouse_rig_state_direction`
- `user.mouse_rig_state_direction_cardinal`
- `user.mouse_rig_state_direction_x`
- `user.mouse_rig_state_direction_y`
- `user.mouse_rig_state_is_moving`
- `user.mouse_rig_state_is_scrolling`
- `user.mouse_rig_state_speed`
- `user.mouse_rig_stop`
- `user.mouse_rig_test_toggle_ui`
- `user.mouse_rig_version`
- `user.mouse_rig_wait`

**Settings:**
- `user.mouse_rig_api`
- `user.mouse_rig_frame_interval`
- `user.mouse_rig_manual_movement_timeout_ms`
- `user.mouse_rig_pause_on_manual_movement`
- `user.mouse_rig_scale`
- `user.mouse_rig_scroll_api`
- `user.mouse_rig_smooth_delta_easing`
- `user.mouse_rig_smooth_delta_ms`
- `user.mouse_rig_smooth_move_to_easing`
- `user.mouse_rig_smooth_move_to_ms`
- `user.mouse_rig_smooth_scroll_easing`
- `user.mouse_rig_smooth_scroll_ms`
- `user.mouse_rig_smooth_speed_easing`
- `user.mouse_rig_smooth_speed_ms`
- `user.mouse_rig_smooth_turn_easing`
- `user.mouse_rig_smooth_turn_ms`

</details>

---


### talon-gamepad-rig

🔗 **GitHub:** [rokubop/talon-gamepad-rig](https://github.com/rokubop/talon-gamepad-rig)

![Version](https://img.shields.io/badge/version-0.8.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-gamepad-rig?style=social)

All purpose gamepad rig with advanced stick manipulation and button handling, for Talon.

| | |
|---|---|
| **Namespace** | `user.gamepad_rig` |
| **Dependencies** | [talon-rig-core](#talon-rig-core) `v0.5.0` |
| **Dev Dependencies** | [community](https://github.com/talonhub/community), [talon-ui-elements](#talon-ui-elements) `v0.15.0` |
| **Pip Dependencies** | [vgamepad](https://pypi.org/project/vgamepad/) |
| **Contributes** | 13 actions, 2 settings |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.gamepad_rig`
- `user.gamepad_rig_button_press`
- `user.gamepad_rig_button_release`
- `user.gamepad_rig_connect`
- `user.gamepad_rig_disconnect`
- `user.gamepad_rig_is_active`
- `user.gamepad_rig_is_connected`
- `user.gamepad_rig_reload`
- `user.gamepad_rig_reset`
- `user.gamepad_rig_state`
- `user.gamepad_rig_stop`
- `user.gamepad_rig_tests`
- `user.gamepad_rig_version`

**Settings:**
- `user.gamepad_rig_stick_deadzone`
- `user.gamepad_rig_trigger_deadzone`

</details>

---


### talon-input-map

🔗 **GitHub:** [rokubop/talon-input-map](https://github.com/rokubop/talon-input-map/)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-input-map?style=social)

This is an alternate way to define your input commands in a way that supports combos, throttling, debounce, switching out configs easily without needing to create new modes. Works with parrot noises, foot pedals, face tracking, or any other input source.

<img src="https://raw.githubusercontent.com/rokubop/talon-input-map/main/preview.svg">

| | |
|---|---|
| **Namespace** | `user.input_map` |
| **Tags** | parrot, noise, foot pedal, face |
| **License** | MIT |
| **Contributes** | 44 actions, 2 settings |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.input_map`
- `user.input_map_channel_event_register`
- `user.input_map_channel_event_unregister`
- `user.input_map_channel_get`
- `user.input_map_channel_get_legend`
- `user.input_map_channel_handle`
- `user.input_map_channel_handle_bool`
- `user.input_map_channel_handle_parrot`
- `user.input_map_channel_handle_value`
- `user.input_map_channel_handle_xy`
- `user.input_map_channel_list`
- `user.input_map_channel_mode_cycle`
- `user.input_map_channel_mode_get`
- `user.input_map_channel_mode_revert`
- `user.input_map_channel_mode_set`
- `user.input_map_channel_register`
- `user.input_map_channel_unregister`
- `user.input_map_event_register`
- `user.input_map_event_unregister`
- `user.input_map_get`
- `user.input_map_get_legend`
- `user.input_map_get_talon_commands`
- `user.input_map_handle`
- `user.input_map_handle_bool`
- `user.input_map_handle_parrot`
- `user.input_map_handle_value`
- `user.input_map_handle_xy`
- `user.input_map_mode_cycle`
- `user.input_map_mode_get`
- `user.input_map_mode_revert`
- `user.input_map_mode_set`
- `user.input_map_reset`
- `user.input_map_single`
- `user.input_map_single_bool`
- `user.input_map_single_get_legend`
- `user.input_map_single_mode_cycle`
- `user.input_map_single_mode_get`
- `user.input_map_single_mode_revert`
- `user.input_map_single_mode_set`
- `user.input_map_single_parrot`
- `user.input_map_single_value`
- `user.input_map_single_xy`
- `user.input_map_tests`
- `user.input_map_version`

**Settings:**
- `user.input_map_combo_window`
- `user.input_map_edge_debounce_ms`

</details>

---


### talon-noise-map

🔗 **GitHub:** [rokubop/talon-noise-map](https://github.com/rokubop/talon-noise-map)

![Version](https://img.shields.io/badge/version-0.5.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-noise-map?style=social)

Advanced remapping for your default Talon pop and hiss noises, using talon-input-map

| | |
|---|---|
| **Namespace** | `user.noise_map` |
| **Dependencies** | [talon-input-map](#talon-input-map) `v1.0.0` |
| **Contributes** | 13 actions, 1 tags |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.noise_map`
- `user.noise_map_disable`
- `user.noise_map_enable`
- `user.noise_map_event_register`
- `user.noise_map_event_unregister`
- `user.noise_map_get`
- `user.noise_map_get_legend`
- `user.noise_map_mode_cycle`
- `user.noise_map_mode_get`
- `user.noise_map_mode_revert`
- `user.noise_map_mode_set`
- `user.noise_map_reset`
- `user.noise_map_version`

**Tags:**
- `user.noise_map_active`

</details>

---


### talon-stable-input

🔗 **GitHub:** [rokubop/talon-stable-input](https://github.com/rokubop/talon-stable-input)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-stable-input?style=social)

Bind keys or pedals to Talon actions that won't be interrupted by voice commands.  Uses pynput.

<img src="https://raw.githubusercontent.com/rokubop/talon-stable-input/main/preview.svg">

| | |
|---|---|
| **Namespace** | `user.stable_input` |
| **Tags** | stable, input, pedal, keys |
| **License** | MIT |
| **Contributes** | 13 actions |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.stable_input_1_down`
- `user.stable_input_1_up`
- `user.stable_input_2_down`
- `user.stable_input_2_up`
- `user.stable_input_3_down`
- `user.stable_input_3_up`
- `user.stable_input_4_down`
- `user.stable_input_4_up`
- `user.stable_input_disable`
- `user.stable_input_enable`
- `user.stable_input_is_enabled`
- `user.stable_input_is_held`
- `user.stable_input_version`

</details>

---


### talon-parrot-rig

🔗 **GitHub:** [rokubop/talon-parrot-rig](https://github.com/rokubop/talon-parrot-rig)

![Version](https://img.shields.io/badge/version-1.4.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-parrot-rig?style=social)

A general-purpose 14-noise parrot mode for hands-free mouse control in Talon.

<img src="https://raw.githubusercontent.com/rokubop/talon-parrot-rig/main/preview.png" width="450">

| | |
|---|---|
| **Namespace** | `user.parrot_rig` |
| **Tags** | parrot, mouse |
| **License** | Unlicense |
| **Requires** | Eye Tracker, Parrot, Talon Beta |
| **Dependencies** | [talon-input-map](#talon-input-map) `v1.0.0`, [talon-mouse-rig](#talon-mouse-rig) `v4.1.0`, [talon-rig-core](#talon-rig-core) `v0.5.0`, [talon-ui-elements](#talon-ui-elements) `v0.15.0` |
| **Contributes** | 45 actions, 1 modes |

<details>
<summary>View all contributions</summary>

**Actions:**
- `user.parrot_rig_boost_long`
- `user.parrot_rig_burst_or_brake`
- `user.parrot_rig_burst_or_brake_stop`
- `user.parrot_rig_click`
- `user.parrot_rig_click_exit`
- `user.parrot_rig_disable`
- `user.parrot_rig_disable_modifiers`
- `user.parrot_rig_enable`
- `user.parrot_rig_exit`
- `user.parrot_rig_get_mode`
- `user.parrot_rig_get_state`
- `user.parrot_rig_move`
- `user.parrot_rig_move_or_slow`
- `user.parrot_rig_reload`
- `user.parrot_rig_repeat_command`
- `user.parrot_rig_repeat_phrase`
- `user.parrot_rig_reset_speed_level`
- `user.parrot_rig_reverse_command`
- `user.parrot_rig_reverse_phrase`
- `user.parrot_rig_scroll`
- `user.parrot_rig_scroll_boost_long`
- `user.parrot_rig_scroll_burst_or_brake`
- `user.parrot_rig_scroll_burst_or_brake_stop`
- `user.parrot_rig_scroll_move`
- `user.parrot_rig_scroll_move_or_slow`
- `user.parrot_rig_scroll_ramp`
- `user.parrot_rig_scroll_resume`
- `user.parrot_rig_scroll_stop`
- `user.parrot_rig_scroll_stop_stay`
- `user.parrot_rig_scroll_stop_temp`
- `user.parrot_rig_scroll_toggle_glide`
- `user.parrot_rig_scroll_tracking_activate`
- `user.parrot_rig_show_help`
- `user.parrot_rig_show_utility_selector`
- `user.parrot_rig_simple_click`
- `user.parrot_rig_stop`
- `user.parrot_rig_toggle`
- `user.parrot_rig_toggle_glide`
- `user.parrot_rig_toggle_modifier`
- `user.parrot_rig_toggle_scroll_move`
- `user.parrot_rig_tracking_activate`
- `user.parrot_rig_utility`
- `user.parrot_rig_utility_select`
- `user.parrot_rig_utility_select_close`
- `user.parrot_rig_version`

**Modes:**
- `user.parrot_rig`

</details>

---


---