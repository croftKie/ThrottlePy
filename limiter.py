class Limiter:
    def __init__(self, request_limit, request_period, log_file, blacklist_request_limit, blacklist_duration):
        self.request_limit = request_limit
        self.request_period = request_period 
        self.log_file = log_file
        self.blacklist_request_limit = blacklist_request_limit
        self.blacklist_duration = blacklist_duration

    # Check against throttle limit
    def check_request(self):
        ## check if the incoming IP is in cache
            ## if so, what is counter
                ## if over limit, fail
                ## if below, allow pass, incr 1
        return
    
    # Check the incoming request IP against cache
    def check_incoming_ip_in_cache(self):
        ## return ip state in cache
        return

    # Check for failed requests
    def check_incoming_request(self):
        ## check if current request failed
        ## check why it failed
        ## if meet blacklist conditions and rate
            ## add to blacklist
        return

    # perform blacklist management
    def add_to_blacklist(self):
        ## ip that meets requirements added to blacklist as dict with associated timestamp
        return

    def check_blacklist_cooldown(self):
        ## check for blacklist members that have expired and remove them
        return

    