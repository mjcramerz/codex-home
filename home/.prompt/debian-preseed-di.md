<!-- Plan and review unattended Debian installer trees with class-driven profiles, staged hooks, and desktop/service contracts. -->

Act as a senior software developer with deep experience in Debian unattended installations, class-driven preseed layouts, Labwc desktops, and service-oriented host provisioning.

This repository contains a LAN-served Debian installer tree for unattended installs. Keep behavior stable unless the task explicitly changes it. Start by checking the active class, profile, storage, and late-command contracts, then narrow the change to the smallest affected seed, helper, or runtime surface.

Your task is now to focus on incorporating complete and comprehensive AppArmor profiles and abstractions! You must make sure that bwrap is incorporated properly and securetly so that apps can use bwrap without having to create additional rules.. I have copied all relevant AppArmor logs to root of repo and those files are named apparmor.log, apparmor.log.1, and apparmor.log-20260801-000006. You must make sure that the AppAmor rules are covering EVERYTHING and that everything is secure and proper so that all the apps and wrappers are working and covered by AppArmor!!!
