import React, { Component } from 'react';


export class Qrs extends Component {
    static displayName = Qrs.name;

    constructor(props: any) {
        super(props);
        this.state = { qrCodes: [], loading: true };
    }

    componentDidMount() {
        this.getQrCodes();
    }

    render() {

        const numbers = [1, 2, 3, 4, 5];
        const listItems = numbers.map((number) =>
            <li key={number.toString()}>
                {number}
            </li>);
            
        return (
            <div>
                <ul>{listItems}</ul>
            </div>
        );
    }

    async getQrCodes() {
        try {
            const response = await fetch('api/Qrs');
            const data = await response.json();
            console.log(data);
            this.setState({ qrCodes: data, loading: false });
        } catch (error) {
            console.error(error);
        }
    }
}