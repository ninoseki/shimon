import vue from "@vitejs/plugin-vue";
import path from "path";
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ _, mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  const target = env.BACKEND_URL || "http://127.0.0.1:8000/";
  const port = env.port || 8080;

  return {
    plugins: [vue()],
    server: {
      port,
      proxy: {
        "/api": target,
      },
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
  };
});
