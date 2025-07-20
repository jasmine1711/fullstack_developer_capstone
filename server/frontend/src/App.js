// import LoginPanel from "./components/Login/Login"
// import { Routes, Route } from "react-router-dom";

// function App() {
//   return (
//     <Routes>
//       <Route path="/login" element={<LoginPanel />} />
//     </Routes>
//   );
// }
// export default App;
import { Routes, Route, Navigate } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}
export default App;
