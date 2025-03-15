import "@chatStyles/App.css";
import { Login } from "@chatPages/login/components/Login";

export const App = () => {
  return (
    <div className="flex w-screen h-screen">
      <Login />
    </div>
  );
};
