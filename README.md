# Talon Hub Roku

A collection of my Talon repos for UI, mouse control, input mapping, parrot, and gaming you may find useful.

This is auto-generated from repo manifests.

## Repos

| Name | Description |
|------|-------------|
| <nobr>**[talon-ui-elements](#talon-ui-elements)**</nobr> | Create stateful canvas UIs using HTML/CSS/React-inspired syntax for python. For use with Talon. |
| <nobr>**[talon-pack](#talon-pack)**</nobr> | Catalogs your Talon repo's contributions and dependencies, generates version validation, and updates your README with badges. |
| <nobr>**[talon-parrot-tester](#talon-parrot-tester)**</nobr> | Visual tool for testing parrot integration with Talon |
| <nobr>**[talon-stable-input](#talon-stable-input)**</nobr> | Bind keys or pedals to Talon actions that won't be interrupted by voice commands.  Uses pynput. |

---

## Repo Details


### talon-ui-elements

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


### talon-pack

🔗 **GitHub:** [rokubop/talon-pack](https://github.com/rokubop/talon-pack)

![Version](https://img.shields.io/badge/version-3.0.0-blue) ![Status](https://img.shields.io/badge/status-preview-orange) ![GitHub stars](https://img.shields.io/github/stars/rokubop/talon-pack?style=social)

Catalogs your Talon repo's contributions and dependencies, generates version validation, and updates your README with badges.

<img src="https://raw.githubusercontent.com/rokubop/talon-pack/main/preview.svg" width="400">

| | |
|---|---|
| **Tags** | package, manifest, version, badges |
| **License** | Unlicense |


---


### talon-parrot-tester

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


### talon-stable-input

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


---