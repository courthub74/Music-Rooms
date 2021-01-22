import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
// import HomePage from "./HomePage";
// import RoomJoinPage from "./RoomJoinPage";      These two are put through routing system.  You can raw put them here
// import CreateRoomPage from "./CreateRoomPage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <HomePage />
            </div>
        );
    }
}


//Access the app container on 'frontend'
const appDiv = document.getElementById("app");
render(<App />, appDiv);