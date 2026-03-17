import { useEffect } from "react";
import { useNavigate } from "react-router";
import { useAppKitAccount } from "@reown/appkit/react";
import { Thirdweb_Client } from "../Thirdweb/thirdweb";

interface AuthWrapperProps {
  children: React.ReactNode;
}

function AuthWrapper({ children }: AuthWrapperProps) {
  const navigate = useNavigate();
  const account = useAppKitAccount();

  // ────────────────────────────────────────────────
  //  Recommended: show loading while we detect state
  // ────────────────────────────────────────────────
  if (account.status === "connecting") {
    console.log("connecting");
  }

  // After auto-connect attempt finished:
  //   - status === "connected"  → user is signed in
  //   - status === "disconnected" → not signed in
  useEffect(() => {
    if (account.status === "disconnected") {
      navigate("/");
    }
  }, [account.status]);

  // If we reach here → status === "connected" and account should exist
  if (!account?.address) {
    console.log("no address");
  }

  return <>{children}</>;
}

export default AuthWrapper;
