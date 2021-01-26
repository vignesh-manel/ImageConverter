import { useState, createContext } from 'react';

export const UserContext = createContext(null);

const UserContextProvider = (props) => {
  const [userData, setUserData] = useState({
    token: undefined,
    email: undefined,
	name: undefined
  });

  return (
    <UserContext.Provider value={{userData, setUserData}}>
	{props.children}
    </UserContext.Provider>
  )
}

export default UserContextProvider
