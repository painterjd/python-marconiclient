
from misc import require_authenticated, require_clientid


class Claim(object):

    def __init__(self, conn, href, messages):
        """
        :param: conn The conn to use for manipulating this claim
        :param: href The fully-qualified URL for this claim
        :param: messages A list of messages belonging to this claim
        """
        self._conn = conn
        self._href = href
        self._msgs = messages

    @property
    def messages(self):
        """
        Returns the messages that were associated with
        this claim at creation time.
        """
        return self._msgs

    @require_authenticated
    @require_clientid
    def update(self, ttl, headers):
        """
        Updates this claim with the specified TTL
        """
        body = {"ttl": ttl}
        self._conn._perform_http(
            href=self._href, method='PATCH', body=body, headers=headers)

    @require_authenticated
    @require_clientid
    def release(self, headers):
        """
        Releases the current claim
        """
        self._conn._perform_http(
            href=self._href, method='DELETE', headers=headers)
