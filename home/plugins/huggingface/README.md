# Hugging Face task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [hf-cli](skills/hf-cli/SKILL.md) | Use this skill for hugging Face Hub CLI (`hf`) for downloading, uploading, and managing repositories, models, datasets, and Spaces on the Hugging Face Hub |
| [huggingface-dataset-viewer](skills/huggingface-dataset-viewer/SKILL.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics. |
| [huggingface-datasets](skills/huggingface-datasets/SKILL.md) | Create and manage datasets on Hugging Face Hub |
| [huggingface-evaluation](skills/huggingface-evaluation/SKILL.md) | Use this skill for add and manage evaluation results in Hugging Face model cards |
| [gradio](skills/gradio/SKILL.md) | Build Gradio web UIs and demos in Python |
| [huggingface-jobs](skills/huggingface-jobs/SKILL.md) | Use this skill when users want to run any workload on Hugging Face Jobs infrastructure |
| [huggingface-model-trainer](skills/huggingface-model-trainer/SKILL.md) | Use this skill when users want to train or fine-tune language models using TRL (Transformer Reinforcement Learning) on Hugging Face Jobs infrastructure |
| [huggingface-paper-publisher](skills/huggingface-paper-publisher/SKILL.md) | Use this skill for publish and manage research papers on Hugging Face Hub |
| [huggingface-tool-builder](skills/huggingface-tool-builder/SKILL.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help |
| [huggingface-trackio](skills/huggingface-trackio/SKILL.md) | Use this skill for track and visualize ML training experiments with Trackio |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
