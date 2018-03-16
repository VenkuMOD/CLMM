'''We define a Profile object, which has some attributes read in from
a config file, and others either calculated from Halo attributes and
methods or directly output from a reader object.  Typically, this Profile
object will populate another Halo attribute as Halo.profile.

'''

from _utils import parse_config
from profile_builder import profile_builder

class Profile:
    '''

    This is a superclass of profiles containing everything a profile should have and do.
    needs to have radii, ghat, sigma_ghat, etc.

    Profile in general should contain everything we need to fit a model profile and get a posterior out.

    '''

    def __init__(self, config) :
        parse_config(self, config)

        if Profile.build == True :
            profile_builder[self.profile_builder_name](self)

        pass

    