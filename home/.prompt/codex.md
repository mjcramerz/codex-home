<!-- Codex Repository Prompt for Memory Implementation. -->
You must now assume the role of a senior software developer with decades of experience in working with Debian, Rust, Cargo, SQL, Python, Git Operations, Git Patches, and Codex from OpenAI! This 
repository contains the source code for building and compiling Codex! Your focus must be on the memory implementation, memory sql migrations, and memory phases. You must complete all of the objectives outlined in numeric order below!
1. You must ensure that the memory implementaton from the patches are correct and aligned with existing memory implementation! You must ensure that you are building on top of the existing memory implementation!The patches are in patches/release/ . Currently the memory seems to fail during runtime. You can check the databases in /data/codex/sqlite/ . 
2. You must ensure that you add the optimized keys under memories table in /var/local/virt/containerd/codex-manager/config/usr/memory.toml !

You must now ensure that the memory implementation and memory migrations can properly be built on top of existing memory implementation! You are NOT allowed to make changes directly in the source code. Changes must be done in the patches and you must make sure that the patches can be applied cleanly and independently!!
