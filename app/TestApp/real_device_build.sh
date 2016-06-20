APP_NAME="TestApp"

xcodebuild -target ${APP_NAME} -sdk iphoneos -configuration Debug CODE_SIGN_IDENTITY="iPhone Developer:xiaodumeiren@163.com(9F76CWR538)"
xcrun -sdk iphoneos PackageApplication -v build/Debug-iphoneos/${APP_NAME}.app -o `pwd`/build/Debug-iphoneos/${APP_NAME}.ipa
