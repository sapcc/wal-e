from azure.storage.blob.blockblobservice import BlockBlobService
from wal_e import log_help

logger = log_help.WalELogger(__name__)


# WABS connection requirements are not quite this same as those of
# S3 and so this class is overkill. Implementing for the sake of
# consistency only
class CallingInfo(object):
    """Encapsulate information used to produce a WABS connection.
    """

    def __init__(self, account_name):
        self.account_name = account_name

    def __repr__(self):
        return ('CallingInfo({account_name})'.format(**self.__dict__))

    def __str__(self):
        return repr(self)

    def connect(self, creds):
        """Return an azure BlockBlobService instance.
        """
        return BlockBlobService(account_name=creds.account_name,
                           account_key=creds.account_key,
                           sas_token=creds.access_token,
                           protocol='https')


def from_store_name(container_name):
    """Construct a CallingInfo value from a target container name.
    """
    return CallingInfo(container_name)
