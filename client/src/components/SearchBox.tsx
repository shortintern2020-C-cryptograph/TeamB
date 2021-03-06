import React, {useState} from "react";
import SearchIcon from "@material-ui/icons/Search";
import {fade, Input, Theme} from "@material-ui/core";
import {makeStyles} from "@material-ui/core/styles";
import useReactRouter from "use-react-router";

const useStyles = makeStyles((theme: Theme) => ({
    textField: {
        marginLeft: theme.spacing(1),
        marginRight: theme.spacing(1),
        width: 200,
    },
    search: {
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.25),
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.45),
        },
        marginLeft: 0,
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            marginLeft: theme.spacing(1),
            width: 'auto',
        },
    },
    searchIcon: {
        width: theme.spacing(9),
        height: '100%',
        position: 'absolute',
        pointerEvents: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    inputRoot: {
        color: 'inherit',
        width: '100%',
    },
    inputInput: (props: Props) => ({
        paddingTop: theme.spacing(1),
        paddingRight: theme.spacing(1),
        paddingBottom: theme.spacing(1),
        paddingLeft: theme.spacing(10),
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            width: props.defaultWidth ? props.defaultWidth : 120,
            '&:focus': {
                width: props.focusWidth ? props.focusWidth : 200,
            },
        },
    }),
}));

type Props = {
    defaultWidth?: number;
    focusWidth?: number;
    placeholder: string,
}

export const SearchBox: React.FC<Props> = (props: Props) => {
    const {history} = useReactRouter();
    const classes = useStyles(props);
    const [query, setQuery] = useState("");

    return (
        <div className={classes.search}>
            <div className={classes.searchIcon}>
                <SearchIcon/>
            </div>
            <form onSubmit={() => {
                history.push(`/search/${query}`);
            }}>
                <Input
                    placeholder={props.placeholder}
                    disableUnderline
                    classes={{
                        root: classes.inputRoot,
                        input: classes.inputInput,
                    }}
                    onChange={(event) => setQuery(event.target.value)}
                />
            </form>
        </div>

    )
}