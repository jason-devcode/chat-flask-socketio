import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { App } from "@chatApp/App";

import "@chatStyles/index.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
