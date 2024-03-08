import LoginPanel from "./components/Login/Login"
import RegistrationPanel from "./components/Register/Register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegistrationPanel />} />
    </Routes>
  );
}
export default App;
