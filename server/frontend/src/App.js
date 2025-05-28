import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";
import RegistrationPanel from "./components/Register/Register"

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegistrationPanel />} />
    </Routes>
  );
}
export default App;
