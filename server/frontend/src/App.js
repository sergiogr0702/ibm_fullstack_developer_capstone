import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer"
import SearchCars from "./components/Dealers/SearchCars"
import PostReview from "./components/Dealers/PostReview"
import LoginPanel from "./components/Login/Login"
import RegisterPanel from "./components/Register/Register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPanel />} />
      <Route path="/dealers" element={<Dealers/>} />
      <Route path="/dealer/:id" element={<Dealer/>} />
      <Route path="/postreview/:id" element={<PostReview/>} />
      <Route path="/searchcars/:id" element={<SearchCars/>} />
    </Routes>
  );
}
export default App;
