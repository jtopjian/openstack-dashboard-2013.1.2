import glance

def get_image_quota(project_id):
    import subprocess
    cmd = 'sudo /root/novac/bin/novac quota-image-get %s' % project_id
    image_limit = subprocess.check_output(cmd, shell=True)
    return int(image_limit.strip())

def set_image_quota(project_id, quota):
    import subprocess
    cmd = 'sudo /root/novac/bin/novac quota-image-set %s %s' % (project_id, quota)
    subprocess.check_call(cmd, shell=True)

def get_image_count(project_id, request):
    (all_images, more_images) = glance.image_list_detailed(request)
    images = [im for im in all_images if im.owner == project_id]
    return len(images)

def get_object_mb_quota(project_id):
    import subprocess
    cmd = 'sudo /root/novac/bin/novac quota-object_mb-get %s' % project_id
    object_mb = subprocess.check_output(cmd, shell=True)
    return int(object_mb.strip())

def set_object_mb_quota(project_id, quota):
    import subprocess
    cmd = 'sudo /root/novac/bin/novac quota-object_mb-set %s %s' % (project_id, quota)
    subprocess.check_call(cmd, shell=True)

def get_object_mb_usage(project_id):
    import subprocess
    cmd = 'sudo /root/novac/bin/novac quota-object_mb-usage %s' % project_id
    object_mb_usage = subprocess.check_output(cmd, shell=True)
    return int(object_mb_usage.strip())

def get_expiration_dates():
    dates = {}
    with open('/etc/openstack-dashboard/dair-expiration.txt') as f:
        for line in f:
            line = line.strip()
            if line != "":
                foo = line.split(':')
                dates[foo[0]] = foo[1]
    return dates

def get_expiration_date(project_id):
    dates = get_expiration_dates()
    if project_id in dates:
        return dates[project_id]
    else:
        return "Information not available."

def set_expiration_date(project_id, expiration_date):
    dates = get_expiration_dates()
    dates[project_id] = expiration_date
    with open('/etc/openstack-dashboard/dair-expiration.txt', 'w') as f:
        for k, v in dates.iteritems():
            f.write("%s:%s\n" % (k,v))

def get_start_dates():
    dates = {}
    with open('/etc/openstack-dashboard/start-dates.txt') as f:
        for line in f:
            line = line.strip()
            if line != "":
                foo = line.split(':')
                dates[foo[0]] = foo[1]
    return dates

def get_start_date(project_id):
    dates = get_start_dates()
    if project_id in dates:
        return dates[project_id]
    else:
        return "Information not available."

def set_start_date(project_id, start_date):
    dates = get_start_dates()
    dates[project_id] = start_date
    with open('/etc/openstack-dashboard/start-dates.txt', 'w') as f:
        for k, v in dates.iteritems():
            f.write("%s:%s\n" % (k,v))

def get_dair_notices():
    notices = {}
    with open('/etc/openstack-dashboard/dair-notices.txt') as f:
        for line in f:
            line = line.strip()
            if line != "":
              foo = line.split('::')
              notices[foo[0]] = foo[1]
    return notices

def get_dair_notice(project_id):
    notices = get_dair_notices()
    if project_id in notices:
        return notices[project_id]
    else:
        return ""

def set_dair_notice(project_id, notice):
    notices = get_dair_notices()
    notices[project_id] = notice
    with open('/etc/openstack-dashboard/dair-notices.txt', 'w') as f:
        for k, v in notices.iteritems():
          f.write("%s::%s\n" % (k,v))

def get_reseller_logos():
    logos = {}
    with open('/etc/openstack-dashboard/dair-reseller-logos.txt') as f:
        for line in f:
            line = line.strip()
            if line != "":
                foo = line.split(':')
                logos[foo[0]] = foo[1]
    return logos

def get_reseller_logo(domain):
    import os.path
    if domain not in ['nova-ab', 'nova-qc', 'nova-hl', 'nova-mi']:
        if os.path.isfile('/usr/share/openstack-dashboard/openstack_dashboard/static/dashboard/img/%s.png' % domain):
            return '%s.png' % domain
        else:
            return "Information not available."
    return "Information not available."

def set_reseller_logo(project_id, logo):
    logos = get_reseller_logos()
    logos[project_id] = logo
    with open('/etc/openstack-dashboard/dair-reseller-logos.txt', 'w') as f:
        for k, v in logos.iteritems():
            f.write("%s:%s\n" % (k,v))

def get_reseller_splash(domain):
    import os.path
    if domain not in ['nova-ab', 'nova-qc', 'nova-hl', 'nova-mi']:
        if os.path.isfile('/usr/share/openstack-dashboard/openstack_dashboard/static/dashboard/img/%s-splash.png' % domain):
            return '%s-splash.png' % domain
        else:
            return "Information not available."
    return "Information not available."

def get_used_resources(project_id):
    import subprocess
    resources = {}
    cmd = 'sudo /root/novac/bin/novac quota-get-used-resources %s' % project_id
    x = subprocess.check_output(cmd, shell=True)
    for r in x.split("\n"):
        r = r.strip()
        if r:
            (resource, used) = r.split(' ')
            resources[resource] = used
    return resources
