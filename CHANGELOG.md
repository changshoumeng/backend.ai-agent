Changes
=======

0.9.5 (2017-04-07)
------------------

 - Add PyTorch support.

 - Upgrade aiohttp to v2 and relevant dependencies as well.

0.9.4 (2017-03-19)
------------------

 - Update missing long_description.

0.9.3 (2017-03-19)
------------------

 - Improve packaging: auto-converted README.md as long description and unified
   requirements.txt and setup.py dependencies.

0.9.2 (2017-03-14)
------------------

 - Fix sorna-common requirement version.

0.9.1 (2017-03-14)
------------------

**CHANGES**

 - Separate console output formats for API v1 and v2.

 - Deprecate unused matching option for execution API.

 - Remove control messages in API responses.

0.9.0 (2017-02-27)
------------------

**NEW**

 - PUSH/PULL-based kernel interaction protocol to support streaming outputs.
   This enables interactive input functions and streaming outputs for long-running codes,
   and also makes kernel execution more resilient to network failures.
   (ZeroMQ's REQ/REP sockets break the system if any messages get dropped)

0.8.2 (2017-01-16)
------------------

**FIXES**

 - Fix a typo that generates errors during GPU kernel initialization.

 - Fix regression of '--agent-ip-override' cli option.

0.8.1 (2017-01-10)
------------------

 - Minor internal polishing release.

0.8.0 (2017-01-10)
------------------

**CHANGES**

 - Bump version to 0.8 to match with sorna-manager and sorna-client.

**FIXES**

 - Fix events lost by HTTP connection timeouts when using `docker.events.run()` from aiodocker.
   (it is due to default 5-minute timeout set by aiohttp)

 - Correct task cancellation

0.7.5 (2016-12-01)
------------------

**CHANGES**

 - Add new aliases for "git" kernel: "git-shell" and "shell"

0.7.4 (2016-12-01)
------------------

**CHANGES**

 - Now it uses [aiodocker][aiodocker] instead of [docker-py][dockerpy] to
   prevent timeouts with many concurrent requests.

   NOTE: You need to run `pip install -r requirements.txt` to install the
         non-pip (GitHub) version of aiodocker correctly, before running
         `pip install sorna-agent`.

**FIXES**

 - Fix corner-case exceptions in statistics/heartbeats.

[aiodocker]: https://github.com/achimnol/aiodocker
[dockerpy]: https://github.com/docker/docker-py

0.7.3 (2016-11-30)
------------------

**CHANGES**

 - Increase docker API timeouts.

**FIXES**

 - Fix heartbeats stop working after kernel/agent timeouts.

 - Fix exception logging in the main server loop.

0.7.2 (2016-11-28)
------------------

**FIXES**

 - Hotfix for missing dependency: coloredlogs

0.7.1 (2016-11-27)
------------------

**NEW**

 - `--agent-ip-override` CLI option to override the IP address of agent
   reported to the manager.

0.7.0 (2016-11-25)
------------------

**NEW**

 - Add support for kernel restarts.
   Restarting preserves kernel metadata and its ID, but removes and recreates
   the working volume and the container itself.

 - Add `--debug` option to the CLI command.

0.6.0 (2016-11-14)
------------------

**NEW**

 - Add support for GPU-enabled kernels (using [nvidia-docker plugin][nvdocker]).
   The kernel images must be built upon nvidia-docker's base Ubuntu images and
   have the label "io.sorna.nvidia.enabled" set `yes`.

**CHANGES**

 - Change the agent to add "lablup/" prefix when creating containers from
   kernel image names, to ease setup and running using the public docker
   repository.  (e.g., "lablup/kernel-python3" instead of "kernel-python3")

 - Change the prefix of kernel image labels from "com.lablup.sorna." to
   "io.sorna." for simplicity.

 - Increase the default idle timeout to 30 minutes for offline tutorial/workshops.

 - Limit the CPU cores available in kernel containers.
   It uses an optional "io.sorna.maxcores" label (default is 1 when not
   specified) to determine the requested number of CPU cores in kernels, with a
   hard limit of 4.

   NOTE: You will still see the full count of CPU cores of the underlying
   system when running `os.cpu_count()`, `multiprocessing.cpu_count()` or
   `os.sysconf("SC_NPROCESSORS_ONLN")` because the limit is enforced by the CPU
   affinity mask.  To get the correct result, try
   `len(os.sched_getaffinity(os.getpid()))`.

[nvdocker]: https://github.com/NVIDIA/nvidia-docker


0.5.0 (2016-11-01)
------------------

**NEW**

 - First public release.


<!-- vim: set et: -->
