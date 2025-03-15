import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import tailwindcss from "@tailwindcss/vite";
import path from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),

      // Assets alias paths
      "@chatIcons": path.resolve(__dirname, "src/assets/icons"),
      "@chatStyles": path.resolve(__dirname, "src/assets/styles"),

      // UI alias paths
      "@chatApp": path.resolve(__dirname, "src/ui/app"),
      "@chatWidgets": path.resolve(__dirname, "src/ui/widgets"),
      "@chatLayouts": path.resolve(__dirname, "src/ui/layouts"),
      "@chatPages": path.resolve(__dirname, "src/ui/pages"),

      // Core alias paths
      "@chatCore": path.resolve(__dirname, "src/core"),
      "@chatInterfaces": path.resolve(__dirname, "src/core/interfaces"),
      "@chatTypes": path.resolve(__dirname, "src/core/types"),
      "@chatUtils": path.resolve(__dirname, "src/core/utils"),
      "@chatApi": path.resolve(__dirname, "src/core/api"),
    },
  },
});
