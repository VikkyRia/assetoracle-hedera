import os
import json
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from kms_manager import KMSManager
#from audit_logger import AuditLogger

load_dotenv()


class HederaSigner:
    """
    Signs Hedera transactions using Mock KMS.
    Fully mocked - no Java or Hedera SDK required.
    In production this would connect to real Hedera network.
    """

    def __init__(self):
        network = os.getenv("HEDERA_NETWORK", "testnet")
        self.operator_account = os.getenv("HEDERA_ACCOUNT_ID", "0.0.1234567")
        self.client = None  # Mock - no real client needed

        self.kms = KMSManager()
        #self.audit = AuditLogger()

        print("✓ Hedera Signer initialized (Mock Mode)")
        print(f"  Network:  {network}")
        print(f"  Operator: {self.operator_account}")
        print("  📝 Note: Production would use real Hedera SDK")

    def get_account_balance(self, account_id=None):
        """Simulate getting Hedera account balance."""
        try:
            if account_id is None:
                account_id = self.operator_account

            mock_balance = "100.00000000 ℏ"
            print(f"✓ Account {account_id} balance: {mock_balance}")
            print("  📝 Note: Production would query real Hedera network")
            return mock_balance

        except Exception as e:
            print(f"✗ Error getting balance: {e}")
            raise

    def create_transfer_transaction(self, to_account, amount_hbar):
        """Simulate creating a Hedera transfer transaction."""
        try:
            print("\n📝 Creating transfer transaction...")
            print(f"  From:   {self.operator_account}")
            print(f"  To:     {to_account}")
            print(f"  Amount: {amount_hbar} HBAR")

            # Mock transaction as a plain dict (no SDK needed)
            transaction = {
                "type": "TRANSFER",
                "from": str(self.operator_account),
                "to": str(to_account),
                "amount": amount_hbar,
                "memo": "AssetOracle - KMS Signed Transaction",
                "timestamp": datetime.now().isoformat(),
            }

            print("✓ Transaction created (mock)")
            return transaction

        except Exception as e:
            print(f"✗ Error creating transaction: {e}")
            raise

    def sign_transaction_with_kms(self, transaction, kms_key_id):
        """
        Sign Hedera transaction using Mock KMS.
        Demonstrates secure signing architecture.
        """
        try:
            print("\n🔐 Signing transaction with Mock KMS...")

            # Serialize transaction dict to bytes and hash it
            transaction_bytes = json.dumps(transaction, sort_keys=True).encode("utf-8")
            transaction_hash = hashlib.sha256(transaction_bytes).digest()

            print(f"  Transaction hash: {transaction_hash.hex()[:16]}...")

            signature = self.kms.sign_data(kms_key_id, transaction_hash)

            print(f"  Signature: {signature.hex()[:16]}...")

           # self.audit.log_key_usage(
               # key_id=kms_key_id,
                ##operation="SIGN_TRANSACTION",
                #details={
                 #   "transaction_hash": transaction_hash.hex(),
                  #  "signature_length": len(signature),
                   # "transaction_type": "TRANSFER",
                #},
            #)

            print("✓ Transaction signed!")
            print("  🔒 Private key never exposed (KMS architecture)")

            return signature

        except Exception as e:
            print(f"✗ Error signing: {e}")
            raise

    def submit_transaction(self, transaction):
        """Simulate submitting transaction to Hedera."""
        try:
            print("\n📤 Submitting to Hedera network (mock)...")

            mock_tx_id = f"0.0.1234567@{int(datetime.now().timestamp())}"
            mock_status = "SUCCESS"
            print("✓ Transaction submitted!")
            print(f"  TX ID:  {mock_tx_id}")
            print(f"  Status: {mock_status}")
            print("  📝 Note: Production would submit to real Hedera network")

            self.audit.log_transaction(
                transaction_id=mock_tx_id,
                status=mock_status,
                details={"timestamp": datetime.now().isoformat()},
            )

            return {
                "transaction_id": mock_tx_id,
                "status": mock_status,
                "timestamp": datetime.now().isoformat(),
            }

        except Exception as e:
            print(f"✗ Error submitting: {e}")
            raise

    def secure_transfer(self, to_account, amount_hbar, kms_key_id):
        """Complete secure transfer using KMS signing."""
        print("\n" + "=" * 60)
        print("SECURE HEDERA TRANSFER WITH MOCK KMS")
        print("=" * 60)

        try:
            print("\n[1/4] Checking balance...")
            self.get_account_balance()

            print("\n[2/4] Creating transaction...")
            transaction = self.create_transfer_transaction(to_account, amount_hbar)

            print("\n[3/4] Signing with Mock KMS...")
            signature = self.sign_transaction_with_kms(transaction, kms_key_id)

            print("\n[4/4] Submitting to Hedera...")
            result = self.submit_transaction(transaction)

            print("\n" + "=" * 60)
            print("✅ SECURE TRANSFER COMPLETE!")
            print("=" * 60)

            return result

        except Exception as e:
            print(f"\n✗ Transfer failed: {e}")
            raise


# ===========================================================================
# SELF-TEST
# ===========================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TESTING HEDERA SIGNER (MOCK MODE)")
    print("=" * 60)

    signer = HederaSigner()
    balance = signer.get_account_balance()

    print("\n✓ Hedera Signer test complete!")
