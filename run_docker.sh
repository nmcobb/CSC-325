# you may need to install readlink - it's on the unix server, but maybe not your system.
docker run -e GRANT_SUDO=yes -v `readlink -m .`:/usr/src/data -p 8889:8889 face_mask_detection
