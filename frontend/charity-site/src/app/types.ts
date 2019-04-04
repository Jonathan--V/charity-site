export type StrStrMap = { [key: string]: string }
export type StrToStrToStrArrMapMap = { [key: string]: StrToStrArrMap }
export type StrToStrArrMap = { [key: string]: string[] }
export type StrToStrToStrMapMap = { [key: string]: StrStrMap }
export type ErrorResponse = StrStrMap | StrToStrToStrArrMapMap | StrToStrToStrMapMap