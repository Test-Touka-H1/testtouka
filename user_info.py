import os
import pwd
import grp

uid = os.getuid()
gid = os.getgid()
user = pwd.getpwuid(uid).pw_name

groups = [grp.getgrgid(g).gr_name for g in os.getgroups()]

print(f"UID: {uid} ({user})")
print(f"GID: {gid}")
print(f"Groups: {', '.join(groups)}")