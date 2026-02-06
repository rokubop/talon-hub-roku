# Talon Hub Roku

A collection of my Talon repos for UI, mouse control, input mapping, parrot, and gaming you may find useful.

This is auto-generated from repo manifests.

## Repos

| Name | Description |
|------|-------------|
| **[talon&#8209;ui&#8209;elements](#talon-ui-elements)** | Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon. |
| **[talon&#8209;pack](#talon-pack)** | Catalogs your Talon repo's contributions and dependencies, generates version validation, and updates your README with badges. |
| **[talon&#8209;parrot&#8209;tester](#talon-parrot-tester)** | Visual tool for testing parrot integration with Talon |
| **[talon&#8209;stable&#8209;input](#talon-stable-input)** | Bind keys or pedals to Talon actions that won't be interrupted by voice commands.  Uses pynput. |
| **[talon&#8209;mouse&#8209;rig](#talon-mouse-rig)** | All purpose mouse rig for Talon with movement and scrolling. Prefers OS-specific relative movement to be compatible with games. |

---

## Repo Details


### talon&#8209;ui&#8209;elements

🔗 **GitHub:** [rokubop/talon-ui-elements](https://github.com/rokubop/talon-ui-elements)

![Version](https://img.shields.io/badge/version-0.14.0-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-ui-elements?style=social)

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


### talon&#8209;pack

🔗 **GitHub:** [rokubop/talon-pack](https://github.com/rokubop/talon-pack)

![Version](https://img.shields.io/badge/version-3.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-pack?style=social)

Catalogs your Talon repo's contributions and dependencies, generates version validation, and updates your README with badges.

<img src="https://raw.githubusercontent.com/rokubop/talon-pack/main/preview.svg" width="400">

| | |
|---|---|
| **Tags** | package, manifest, version, badges |
| **License** | Unlicense |


---


### talon&#8209;parrot&#8209;tester

🔗 **GitHub:** [rokubop/talon-parrot-tester](https://github.com/rokubop/talon-parrot-tester)

![Version](https://img.shields.io/badge/version-0.8.0-blue) ![Status](https://img.shields.io/badge/status-stable-green) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-parrot-tester?style=social)

Visual tool for testing parrot integration with Talon

<img src="https://raw.githubusercontent.com/rokubop/talon-parrot-tester/main/preview.png" width="400">

| | |
|---|---|
| **Namespace** | `user.parrot_tester` |
| **Tags** | parrot |
| **License** | MIT |
| **Dependencies** | talon-ui-elements `v0.14.0` |
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


### talon&#8209;stable&#8209;input

🔗 **GitHub:** [rokubop/talon-stable-input](https://github.com/rokubop/talon-stable-input)

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-stable-input?style=social)

Bind keys or pedals to Talon actions that won't be interrupted by voice commands.  Uses pynput.

<img src="https://raw.githubusercontent.com/rokubop/talon-stable-input/main/preview.svg" width="400">

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


### talon&#8209;mouse&#8209;rig

🔗 **GitHub:** [rokubop/talon-mouse-rig](https://github.com/rokubop/talon-mouse-rig)

![Version](https://img.shields.io/badge/version-0.6.0-blue) ![Status](https://img.shields.io/badge/status-experimental-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-mouse-rig?style=social)

All purpose mouse rig for Talon with movement and scrolling. Prefers OS-specific relative movement to be compatible with games.

<img src="https://raw.githubusercontent.com/rokubop/talon-mouse-rig/main/preview.svg" width="400">

| | |
|---|---|
| **Namespace** | `user.mouse_rig` |
| **Tags** | mouse, movement |
| **License** | MIT |
| **Dev Dependencies** | talon-ui-elements `v0.14.0` |
| **Contributes** | 47 actions, 5 settings |

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
- `user.mouse_rig_scroll_by`
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
- `user.mouse_rig_scroll_speed_add`
- `user.mouse_rig_scroll_speed_mul`
- `user.mouse_rig_scroll_speed_to`
- `user.mouse_rig_scroll_stop`
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


---