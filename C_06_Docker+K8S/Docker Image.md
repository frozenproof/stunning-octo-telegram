# Where are the docker images?
1. Linux
On Linux systems, Docker images are typically stored in:

Default Storage Location: **/var/lib/docker**
Inside this directory, you’ll find various subdirectories, including:

**/var/lib/docker/overlay2/**: This is where the file system layers of the images are stored if you're using the overlay2 storage driver (which is the default for most modern Docker installations).

**/var/lib/docker/containers/**: This contains data about running and stopped containers, including logs.

2. Windows and macOS
On Windows and macOS, Docker uses a lightweight virtual machine to run the Docker daemon. Images are stored in the virtual machine’s file system, which is abstracted away from the host operating system. However, you can generally manage Docker images and containers using the Docker CLI without needing to access these files directly.