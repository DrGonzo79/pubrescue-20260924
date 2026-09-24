import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {title:"PubRescue — Publisher migration audit",description:"Audit a fictional Microsoft Publisher file inventory and build a migration runbook."};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
