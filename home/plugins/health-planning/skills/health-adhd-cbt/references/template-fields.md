---
title: ADHD + CBT template fields
status: active
owner: Matthew Cramer
tags:
- skills
- all
- health-adhd-cbt
- references
- template-fields-md
- template-fields
- admin
updated: '2026-02-20'
---
# ADHD + CBT template fields

## Source
- Canonical PDF reference: `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/assets/source/Concise_ADHD_CBT_Daily_Templates_A4_FINAL_COMPLETE_v2.pdf`
- HTML templates: `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/assets/templates/`
- CSS: `$CODEX_HOME/plugins/cache/codex-home/health-planning/1.0.0/skills/health-adhd-cbt/assets/styles/pdf.css`

## Rendering safety notes
- Placeholder keys must use identifier-style names (`[A-Za-z_][A-Za-z0-9_]*`).
- Placeholder values are rendered as escaped text (not raw HTML) to avoid script/style injection.
- Very large payloads are rejected by renderer size limits.

## Templates included
- `daily-flow.html` - daily launch, top outcomes, midday reset, shutdown, micro habits
- `daily-focus.html` - focus sprint planning and distraction supports
- `decisions-impulses.html` - shiny object parking lot, decision filter, email helper
- `emotions-self-management.html` - CBT thought check, regret reset, HALT basics, wind-down
- `weekly-plan.html` - weekly outcomes, schedule anchors, energy plan
- `task-breakdown.html` - task decomposition and next actions
- `habit-tracker.html` - 2-week habit tracker grid
- `monthly-review.html` - monthly review, wins, challenges, and next priorities
- `appointment-prep.html` - appointment goals, questions, and logistics
- `sensory-reset.html` - sensory regulation checklist and reset plan
- `daily-pack.html` - original three templates in one PDF (page breaks)

## Placeholders (by template)

### Shared
- `day`
- `date`

### daily-flow.html
- `energy_am`
- `direction_am`
- `done_definition`
- `top_1`
- `top_2`
- `top_3`
- `first_tiny_action`
- `timebox`
- `blocker`
- `anchor`
- `sprint_notes`
- `next_step`
- `reward`
- `midday_now`
- `win_1`
- `win_2`
- `win_3`
- `unfinished`
- `single_next`
- `park_idea`
- `quick_reset`
- `return_to_task`
- `tomorrow_first`
- `shutdown_notes`

### decisions-impulses.html
- `idea`
- `trigger`
- `exciting_reason`
- `body_signal`
- `cost`
- `urge`
- `drop_item`
- `future_me_choice`
- `decision`
- `scheduled`
- `delay_plan`
- `after_delay`
- `parking_notes`
- `next_step_decision`
- `decision_timebox`
- `decision_notes`
- `email_decision`
- `email_recipients`
- `email_value`
- `email_goal`
- `email_subject`
- `email_context`
- `email_point_1`
- `email_point_2`
- `email_point_3`
- `email_ask`
- `email_draft`

### daily-focus.html
- `focus_goal`
- `focus_done`
- `focus_start`
- `focus_end`
- `block_1`
- `block_2`
- `block_3`
- `distraction_plan`
- `parking_lot`
- `support`
- `environment`
- `break_plan`
- `reward_focus`
- `wrap_notes`

### emotions-self-management.html
- `situation`
- `emotion_intensity`
- `automatic_thought`
- `evidence_for`
- `evidence_against`
- `balanced_thought`
- `compassion_line`
- `next_action`
- `cbt_notes`
- `what_happened`
- `repair_step`
- `lesson`
- `system_tweak`
- `tiny_fix`
- `shutdown_time`
- `screens_off`
- `brain_dump`
- `tomorrow_top`
- `wind_down_notes`

### weekly-plan.html
- `week_of`
- `weekly_theme`
- `weekly_top_1`
- `weekly_top_2`
- `weekly_top_3`
- `weekly_first_step`
- `appointments`
- `deadlines`
- `support_week`
- `energy_plan`
- `rest_plan`
- `boundaries`
- `wins_week`
- `review_notes`
- `next_week_seed`

### task-breakdown.html
- `task_name`
- `task_done`
- `task_why`
- `time_estimate`
- `start_trigger`
- `step_1`
- `step_2`
- `step_3`
- `step_4`
- `step_5`
- `step_6`
- `blockers`
- `support_tools`
- `reward_task`
- `next_action`

### habit-tracker.html
- `week_of`
- `focus_habit`
- `habit_1`
- `habit_2`
- `habit_3`
- `habit_4`
- `habit_notes`

### monthly-review.html
- `month_of`
- `review_date`
- `win_1`
- `win_2`
- `win_3`
- `win_4`
- `win_5`
- `challenge_1`
- `challenge_2`
- `challenge_3`
- `helped_most`
- `not_helped`
- `habit_1`
- `habit_2`
- `habit_3`
- `habit_keep`
- `habit_adjust`
- `energy_avg`
- `sleep_avg`
- `focus_blocks`
- `meds_consistency`
- `movement_days`
- `next_priority_1`
- `next_priority_2`
- `next_priority_3`
- `next_first_step`
- `support_needed`
- `boundaries`
- `carryover_1`
- `carryover_2`
- `carryover_3`
- `monthly_notes`

### appointment-prep.html
- `appointment_type`
- `provider_name`
- `appointment_date`
- `appointment_time`
- `appointment_location`
- `goal_1`
- `goal_2`
- `goal_3`
- `question_1`
- `question_2`
- `question_3`
- `question_4`
- `question_5`
- `symptoms`
- `meds_updates`
- `side_effects`
- `life_changes`
- `whats_working`
- `accommodations`
- `support_person`
- `follow_up`
- `after_tasks`
- `follow_up_date`

### sensory-reset.html
- `day`
- `date`
- `overwhelm_level`
- `energy_level`
- `trigger`
- `body_signals`
- `light_adjust`
- `sound_adjust`
- `temp_adjust`
- `texture_adjust`
- `space_change`
- `grounding_exercise`
- `movement`
- `hydrate_snack`
- `return_action`
- `support`
- `sensory_notes`

## Notes
- All placeholders are optional. Missing keys are rendered as blank lines.
- The templates are designed for printing and handwriting, but can be prefilled via JSON.
