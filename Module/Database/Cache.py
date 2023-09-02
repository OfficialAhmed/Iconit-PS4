"""
    Classes handle FTP Caching.

    UPLOAD/DOWNLOAD Iconit cache for better performance

    TODO:
        * prompt user before starting process
        * UPLOAD -> upload cached files to ps4 
        * DOWNLOAD -> overwrite local cached files 
        * on ps4 connect check for old version cache
        * option to manually cache data to ps4
"""

from environment import Common


class PS4(Common):

    def __init__(self) -> None:
        self.ftp = self.get_ftp()

    def check(self):
        """ 
        ### Check wether cache folder exists on PS4\n 
            * notify user 
        """
        self.ftp.cwd(self.ps4_cache_path)

    def upload(self):
        """ 
        ### Store cache on PS4\n 
            * prompt user for permission/overwrite 
        """
        pass

    def download(self):
        """ 
        ### Retreive cached folder from PS4\n 
            * prompt user for overwrite
        """
        pass
