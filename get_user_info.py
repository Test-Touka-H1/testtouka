import os
import pwd
import grp
import getpass

def get_user_info():
    user = getpass.getuser()
    pw_record = pwd.getpwnam(user)
    
    uid = pw_record.pw_uid
    gid = pw_record.pw_gid
    home = pw_record.pw_dir
    shell = pw_record.pw_shell
    
    # Get all groups the user belongs to
    groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
    
    # Also include the primary group
    try:
        primary_group = grp.getgrgid(gid).gr_name
        if primary_group not in groups:
            groups.insert(0, primary_group)
    except KeyError:
        primary_group = "Unknown"
    
    # Display
    print(f"Username: {user}")
    print(f"UID     : {uid}")
    print(f"GID     : {gid}")
    print(f"Groups  : {', '.join(groups)}")
    print(f"Home Dir: {home}")
    print(f"Shell   : {shell}")

if __name__ == "__main__":
    get_user_info()