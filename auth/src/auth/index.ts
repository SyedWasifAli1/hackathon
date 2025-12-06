// Better Auth setup for Physical AI & Humanoid Robotics Textbook
import { betterAuth } from "better-ai";

export const auth = betterAuth({
  database: {
    url: process.env.DATABASE_URL!,
    type: "postgresql", // or "mysql"
  },
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: false,
  },
  socialProviders: {
    // Add social providers if needed
  },
  advanced: {
    // Custom session handling if needed
  },
});