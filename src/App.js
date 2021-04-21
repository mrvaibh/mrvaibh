import './App.css';

// Router
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

// Components
import Header from "./components/Header";
import Footer from "./components/Footer";
import NotFound404 from "./components/NotFound404";
import BackToTop from "./components/BackToTop";
import Home from "./components/Home/Home"
import About from "./components/About/About"

function App() {
  return (
    <Router>
      <div className="App">
        <Header active="hello" />

        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about" render={About} />
          <Route path="" render={NotFound404} />
        </Switch>


        <Footer />

        <BackToTop />

      </div>
    </Router>

  );
}

export default App;
