import React, { useContext } from "react";
import './App.css';
import Login from "./components/Login";
import Signup from "./components/Signup";
import Home from "./components/Home";
import {UserContext} from './context/UserContext';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";

function App() {
	
  const { userData } = useContext(UserContext);	
	
  return (
    <div className="App">
      <Router>
		{!userData.token ? (
			<div>
				<Route exact path={["/","/login"]}><Login /></Route>
				<Route path="/signup"><Signup /></Route>
			</div>
		): (
			<div className="app_body">
				<Switch>
					<Route path="/">
						<Home />
					</Route>
		  </Switch>

	  </div>   
	)}
	     </Router>
    </div>
  );
}

export default App;
