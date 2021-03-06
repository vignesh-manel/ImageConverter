import React, { useState, useEffect } from "react";
import "./Signup.css";
import axios from '../axios';
import ErrorMessage from "./ErrorMessage";
import { Link, useHistory } from "react-router-dom";

function Signup() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [name, setName] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const history = useHistory();

    const sleep = (ms) => {
	return new Promise(resolve => setTimeout(resolve, ms));
    }

    //signup user and redirect to login page
    const signup = async (e) => {

	e.preventDefault();
	try {
		await axios.post('/users/register', {
		    email: email,
		    password: password,
		    confirmPassword: confirmPassword,
		    name: name
		});
		setSuccess(true);
		await sleep(2000);
		history.push("/");

	}
	catch (err) {
	    err.response.data.msg && setError(err.response.data.msg)
	}

    }

    return (
	<div className="signup">
	    <div className="signup_container">
		<img src="" alt=""/>
		<div className="signup_text">
		    <h1>Register to ImageConverter</h1>
		</div>

		{success && <div className="successMessage">
		    <span>Successfully Registered</span>
		</div>
		}


		{error && <ErrorMessage message={error} clearError={() => setError(undefined)} />}
		<div className="signup_form">
		    <form>
		        <input
			    placeholder="Enter your email id"
			    type="text"
			    onChange={(e) => setEmail(e.target.value)}
		        />
		        <input 
			    placeholder="Enter your password"
			    type="password"
			    onChange={(e) => setPassword(e.target.value)}
		        />
		        <input 
			    placeholder="Re-enter your password"
			    type="password"
			    onChange={(e) => setConfirmPassword(e.target.value)}
		        />
		        <input 
			    placeholder="Enter your name"
			    type="text"
			    onChange={(e) => setName(e.target.value)}
		        />
		        <button onClick={signup}
			    type="submit">
			    Sign Up
		        </button>
			<h6>Already Registered? <Link to="/">Login</Link></h6>
		   </form>
		</div>
	    </div>
	</div>
    )
}

export default Signup
