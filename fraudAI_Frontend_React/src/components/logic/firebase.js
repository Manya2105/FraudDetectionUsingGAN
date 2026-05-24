// Import Firebase modules
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { getFirestore, doc, getDoc, setDoc } from "firebase/firestore";

// ✅ Your Firebase config (REAL VALUES)
const firebaseConfig = {
  apiKey: "AIzaSyCn-GsZwISexNz_OTCCRPa0U5Cpx5w3xvo",
  authDomain: "sanya-c7626.firebaseapp.com",
  projectId: "sanya-c7626",
  storageBucket: "sanya-c7626.appspot.com",
  messagingSenderId: "752157169467",
  appId: "1:752157169467:web:7b0ce07405fcc6c023c91e",
  measurementId: "G-Y3M6KERK3B"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Export services
export const auth = getAuth(app);
export const db = getFirestore(app);
export const provider = new GoogleAuthProvider();
export { signInWithPopup };