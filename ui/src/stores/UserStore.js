import {Store} from 'overstated';

export default class UserStore extends Store {
    state = {
        loggedIn: false,
    };

    logIn = () => {
        return this.setState({
            loggedIn: true
        })
    };

    logOut = () => {
        return this.setState({
            loggedIn: false
        })
    }
}