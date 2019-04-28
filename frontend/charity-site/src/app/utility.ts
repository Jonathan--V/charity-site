import { ErrorResponse, StrStrMap, StrToStrArrMap } from "./types";

export class Utility {
  static processErrorsMap(errorResponse: ErrorResponse, errorMessage: string): StrStrMap {
    console.error(errorMessage)
    console.error(errorResponse)
    const errors: string | StrToStrArrMap | StrStrMap = errorResponse['error']
    let result: StrStrMap = { 'custom': `${errorMessage}:` }
    if (typeof errorResponse['detail'] === "string") {
      result['response_detail'] = String(errorResponse['detail'])
    }
    if (typeof errors === "string") {
      result['error'] = errors
    }
    else if (typeof errorResponse['message'] === "string"
      && String(errorResponse['message']).endsWith(': 0 Unknown Error')) {
      result['backend_unavailable'] = "Unable to contact backend server."
    }
    else {
      for (let [key, item] of Object.entries(errors)) {
        if (typeof item === "string") {
          result[key] = item
        }
        else if (Array.isArray(item)) {
          result[key] = item.join('\n')
        }
        else {
          throw new Error(`Error messages are of unexpected type. Item is: ${item}`);
        }
      }
    }
    for (let [key, value] of Object.entries(result)){
      result[key] = value.replace(/<(?:.|\n)*?>/gm, '')
    }
    return result
  }

  static processErrors(errorResponse: ErrorResponse, errorMessage: string): string[] {
    return Object.values(this.processErrorsMap(errorResponse, errorMessage))
  }
}
