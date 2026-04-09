import json
import os
from datetime import datetime

class AuditLogger:
    """Logs all key usage and transactions for compliance"""
    
    def init(self, log_file="audit_logs.json"):
        self.log_file = log_file
        self.logs = self._load_logs()
        print(f"✓ Audit Logger initialized")
    
    def _load_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_logs(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)
    
    def log_key_usage(self, key_id, operation, details=None):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': 'KEY_USAGE',
            'key_id': key_id,
            'operation': operation,
            'details': details or {}
        }
        
        self.logs.append(log_entry)
        self._save_logs()
        print(f"📝 Logged: {operation}")
    
    def log_transaction(self, transaction_id, status, details=None):
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': 'TRANSACTION',
            'transaction_id': transaction_id,
            'status': status,
            'details': details or {}
        }
        
        self.logs.append(log_entry)
        self._save_logs()
        print(f"📝 Logged: Transaction {transaction_id}")
    
    def get_recent_logs(self, count=10):
        return self.logs[-count:]
    
    def print_audit_report(self):
        print("\n" + "="*60)
        print("AUDIT REPORT")
        print("="*60)
        
        total = len(self.logs)
        key_usage = sum(1 for log in self.logs if log['type'] == 'KEY_USAGE')
        transactions = sum(1 for log in self.logs if log['type'] == 'TRANSACTION')
        
        print(f"\nTotal Events: {total}")
        print(f"  Key Usage: {key_usage}")
        print(f"  Transactions: {transactions}")
        
        print(f"\nRecent Events:")
        for log in self.get_recent_logs(5):
            print(f"\n  [{log['timestamp']}]")
            print(f"  Type: {log['type']}")
        
        print("\n" + "="*60)


if __name__ == "__main__":
    logger = AuditLogger()
    logger.log_key_usage("test-key", "SIGN", {"test": True})
    logger.print_audit_report()
