
import os
import json
import hashlib
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import secrets

class KMSManager:
    """
    Simulates AWS KMS operations locally
    In production, this would connect to real AWS KMS
    """
    
    def __init__(self):
        self.keys_file = "local_kms_keys.json"
        self.keys = self._load_keys()
        print(f"✓ Mock KMS Manager initialized (Local Simulation)")
        print(f"  📝 Note: Production would use real AWS KMS")
    
    def _load_keys(self):
        """Load stored keys from file"""
        if os.path.exists(self.keys_file):
            with open(self.keys_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_keys(self):
        """Save keys to file"""
        with open(self.keys_file, 'w') as f:
            json.dump(self.keys, f, indent=2)
    
    def create_key(self, description="Hedera Transaction Signing Key"):
        """
        Simulate creating a KMS key
        
        Args:
            description: Description of the key's purpose
            
        Returns:
            dict: Key metadata including KeyId
        """
        try:
            print(f"\n🔑 Creating mock KMS key: {description}")
            
            # Generate ECDSA key pair (same as AWS KMS would use)
            private_key = ec.generate_private_key(
                ec.SECP256K1(),  # Hedera-compatible curve
                default_backend()
            )
            
            # Generate unique Key ID
            key_id = f"mock-kms-{secrets.token_hex(16)}"
            
            # Serialize keys for storage
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8, 
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8')
            
            public_key = private_key.public_key()
            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')
            
            # Store key
            self.keys[key_id] = {
                'KeyId': key_id,
                'Description': description,
                'CreationDate': datetime.now().isoformat(),
                'Enabled': True,
                'KeyState': 'Enabled',
                'PrivateKey': private_pem,
                'PublicKey': public_pem
            }
            
            self._save_keys()
            
            print(f"✓ Mock KMS Key created successfully!")
            print(f"  Key ID: {key_id}")
            print(f"  🔒 Private key securely stored locally")
            print(f"  📝 In production: Key would be in AWS KMS hardware")
            
            return {
                'KeyId': key_id,
                'Arn': f"arn:aws:kms:us-east-1:mock:key/{key_id}",
                'Description': description
            }
            
        except Exception as e:
            print(f"✗ Error creating key: {str(e)}")
            raise
    
    def get_public_key(self, key_id):
        """
        Get public key
        
        Args:
            key_id: Key ID
            
        Returns:
            bytes: Public key in PEM format
        """
        try:
            if key_id not in self.keys:
                raise ValueError(f"Key not found: {key_id}")
            
            public_key_pem = self.keys[key_id]['PublicKey']
            print(f"✓ Retrieved public key for: {key_id[:20]}...")
            return public_key_pem.encode('utf-8')
            
        except Exception as e:
            print(f"✗ Error getting public key: {str(e)}")
            raise
    
    def sign_data(self, key_id, message):
        """
        Sign data using stored private key
        Simulates AWS KMS signing operation
        
        Args:
            key_id: Key ID
            message: Data to sign (bytes)
            
        Returns:
            bytes: Digital signature
        """
        try:
            print(f"\n🔐 Signing data with mock KMS key...")
            
            if key_id not in self.keys:
                raise ValueError(f"Key not found: {key_id}")
            
            # Load private key
            private_pem = self.keys[key_id]['PrivateKey']
            private_key = serialization.load_pem_private_key(
                private_pem.encode('utf-8'),
                password=None,
                backend=default_backend()
            )
            
            # Sign the message
            signature = private_key.sign(
                message,
                ec.ECDSA(hashes.SHA256())
            )
            
            print(f"✓ Data signed successfully!")
            print(f"  Signature length: {len(signature)} bytes")
            print(f"  📝 In production: Signing would happen inside AWS KMS")
            
            return signature
            
        except Exception as e:
            print(f"✗ Error signing data: {str(e)}")
            raise
    
    def enable_key_rotation(self, key_id):
        """Simulate enabling key rotation"""
        print(f"✓ Key rotation enabled for: {key_id[:20]}...")
        print(f"  📝 In production: AWS KMS would auto-rotate annually")
    
    def get_key_info(self, key_id):
        """
        Get key metadata
        
        Args:
            key_id: Key ID
            
        Returns:
            dict: Key information
        """
        try:
            if key_id not in self.keys:
                raise ValueError(f"Key not found: {key_id}")
            
            key_data = self.keys[key_id]
            
            return {
                'KeyId': key_data['KeyId'],
                'Arn': f"arn:aws:kms:us-east-1:mock:key/{key_id}",
                'CreationDate': key_data['CreationDate'],
                'Enabled': key_data['Enabled'],
                'Description': key_data.get('Description', 'N/A'),
                'KeyState': key_data['KeyState']
            }
            
        except Exception as e:
            print(f"✗ Error getting key info: {str(e)}")
            raise
    
    def list_keys(self):
        """List all stored keys"""
        keys = [{'KeyId': k} for k in self.keys.keys()]
        
        print(f"\n✓ Found {len(keys)} mock KMS keys")
        for key in keys:
            print(f"  - {key['KeyId'][:40]}...")
        
        return keys


# TEST THE MOCK KMS MANAGER
if __name__ == "__main__":
    print("="*60)
    print("TESTING MOCK AWS KMS MANAGER")
    print("="*60)
    
    kms = KMSManager()
    
    # Test 1: Create a new key
    print("\n[TEST 1] Creating new mock KMS key...")
    key_info = kms.create_key("Hedera Transaction Signing Key - Test")
    
    key_id = key_info['KeyId']
    
    # Test 2: Get public key
    print("\n[TEST 2] Retrieving public key...")
    public_key = kms.get_public_key(key_id)
    print(f"Public key size: {len(public_key)} bytes")
    
    # Test 3: Sign sample data
    print("\n[TEST 3] Signing sample data...")
    test_message = b"Hello from AssetOracle!"
    signature = kms.sign_data(key_id, test_message)
    print(f"Signature generated: {signature[:20].hex()}...")
    
    # Test 4: Enable key rotation
    print("\n[TEST 4] Enabling key rotation...")
    kms.enable_key_rotation(key_id)
    
    # Test 5: Get key details
    print("\n[TEST 5] Getting key information...")
    info = kms.get_key_info(key_id)
    print(json.dumps(info, indent=2))
    
    print("\n" + "="*60)
    print("✓ ALL TESTS PASSED!")
    print("="*60)
    print(f"\n📝 Save this Key ID to your .env file:")
    print(f"KMS_KEY_ID={key_id}")
    print("\n💡 This is a LOCAL SIMULATION of AWS KMS")
    print("   Production version would use real AWS KMS service")
