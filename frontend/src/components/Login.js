import React, { useState, useContext } from "react";
import "./Login.css";
import axios from '../axios';
import {UserContext} from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";
import { Link } from "react-router-dom";

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { setUserData } = useContext(UserContext);
    const [error, setError] = useState('');

    //log in the user and set user data in context
    const login = async (e) => {

	e.preventDefault();
	try {
		const resUser = await axios.post('/users/login', {
		    email: email,
		    password: password
		});
		setUserData({
		    token: resUser.data.token,
		    email: resUser.data.email,
			name: resUser.data.name
		});
	}
	catch (err) {
	    err.response.data.msg && setError(err.response.data.msg)
	}

    }

    return (
	<div className="login">
	    <div className="login_container">
		<img src="" alt=""/>
		<div className="login_text">
		    <h1>Sign in to ImageConverter</h1>
		</div>
		{error && <ErrorMessage message={error} clearError={() => setError(undefined)} />}
		<div className="login_form">
		    <form>
		        <input
			    placeholder="Enter your email id"
			    type="email"
			    onChange={(e) => setEmail(e.target.value)}
		        />
		        <input 
			    placeholder="Enter your password"
			    type="password"
			    onChange={(e) => setPassword(e.target.value)}
		        />
		        <button onClick={login}
			    type="submit">
			    Login
		        </button>
			<h6>Not Registered? <Link to="/signup">Sign up</Link></h6>
		   </form>
		</div>
		<h5>This is a dummy application, do not enter any senstive information</h5>
	    </div>
	</div>
    )
}

export default Login
