import { Routes, Route } from "react-router-dom"

import Layout from "./components/Layout"
import Home from "./pages/Home"
import Invoice from "./pages/Invoice"

import './App.css'
import NotFound from "./pages/NotFound"

function App() {

  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="invoices" element={<Invoice />} />
        {/* Using path="*"" means "match anything", so this route
                    acts like a catch-all for URLs that we don't have explicit
                    routes for. */}
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

export default App