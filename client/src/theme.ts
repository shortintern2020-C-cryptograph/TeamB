import {createMuiTheme, Theme} from "@material-ui/core/styles";
import { lime} from "@material-ui/core/colors";

export const theme:Theme = createMuiTheme({
  palette: {
    primary: {
      light: "#a7ffeb",
      main: lime["A700"],
      dark: "#1E8279",
      contrastText: "#ffffff",
    },
    secondary: {
      light: "#ff9865",
      main: "#ee6738",
      dark: "#b5360a",
      contrastText: "#ffffff",
    },
  },
  typography: {
    fontFamily: [
      "游ゴシック Medium",
      "ＭＳ Ｐゴシック",
      "游ゴシック体",
      "Noto Sans JP",
      "Lato",
      "Yu Gothic Medium",
      "YuGothic",
      "ヒラギノ角ゴ ProN",
      "Hiragino Kaku Gothic ProN",
      "メイリオ",
      "Meiryo",
      "MS PGothic",
      "sans-serif",
    ].join(","),
    fontWeightLight:300,
    fontWeightMedium:400,
    fontWeightBold:500,
  },
});