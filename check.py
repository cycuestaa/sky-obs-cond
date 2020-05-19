import numpy as np

  
    # check clouds from mcnowinski/seo/itzamna/chultun.py 
    # acceptable clouds max = 30%
    def checkClouds(self):
        (output, error, pid) = self.runSubprocess(['tx', 'taux'])
        match = re.search('cloud=([\\-\\.0-9]+)', output)
        if match:
            clouds = float(match.group(1))
            logger.debug('Cloud cover is %d%%.' % int(clouds*100))
            if clouds >= self.max_clouds_slit:
                logger.error(
                    'Too many clouds (%d%%). Aborting image sequence...' % int(clouds*100))
                if not self.simulate:
                    self.done()
            while clouds >= self.max_clouds_image:
                self.slackalert(
                    'Too many clouds (%d%%). Pausing image sequence...' % int(clouds*100))
                self.checkSun()
                self.checkSlit()
                self.checkAlt()
                if self.simulate:
                    break
                time.sleep(30)
                match = re.search('cloud=([\\-\\.0-9]+)', output)
                if match:
                    clouds = float(match.group(1))
                    if clouds >= self.max_clouds_slit:
                        logger.error(
                            'Too many clouds (%d%%). Aborting image sequence...' % int(clouds*100))
                        if not self.simulate:
                            self.done()
                    logger.debug('Cloud cover is %d%%.' % int(clouds*100))
                else:
                    logger.error('Cloud command failed (%s).' % output)
        return True
