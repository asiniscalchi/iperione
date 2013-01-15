import mimetypes

class FileIdentifier:
	def mime(self, url):
		return mimetypes.guess_type(url)[0]

