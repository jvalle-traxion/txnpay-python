class TraxionPayError(Exception):
  pass

class MissingAuthenticationError(TraxionPayError):
  pass

class APIResponseError(TraxionPayError):
  pass