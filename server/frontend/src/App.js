import React from "react";
import LoginPanel from "./components/Login/Login"; // Importing the Login component
import Register from "./components/Register/Register"; // Importing the Register components
import Dealers from './components/Dealers/Dealers';
import Dealer from './components/Dealers/Dealer';
import PostReview from "./components/Dealers/PostReview";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
        <Route path="/login" element={<LoginPanel />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dealers" element={<Dealers/>} />
        <Route path="/dealer/:id" element={<Dealer/>} />
        <Route path="/postreview/:id" element={<PostReview/>} />
    </Routes>
  );
}
export default App;
