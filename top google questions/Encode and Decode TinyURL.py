class Codec:
    def __init__(self):
        self.counts = 0
        self.pool = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        self.com = "http://tinyurl.com/"
        self.map = dict()
        self.revmap = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        def encode_rule(counts):
            res = []
            len_pool = len(self.pool)
            while counts > 0:
                res.append(self.pool[counts%len_pool])
                counts //= len_pool
            return ''.join(res)
        if longUrl not in self.map:
            self.counts += 1
            self.map[longUrl] = self.com + encode_rule(self.counts)
            self.revmap[self.map[longUrl]] = longUrl
        return self.map[longUrl]


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.revmap[shortUrl]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))