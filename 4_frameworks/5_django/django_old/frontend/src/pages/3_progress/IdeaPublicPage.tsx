// TODO download modules ///////////////////////////////////////////////////////////////////////////////////////////////

import React, { FormEvent, MouseEvent, useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Container, Navbar, Nav, NavDropdown } from "react-bootstrap";

// TODO custom modules /////////////////////////////////////////////////////////////////////////////////////////////////

import * as constant from "../../components/constant";
import * as hook from "../../components/hook";
import * as util from "../../components/util";
import * as slice from "../../components/slice";

import * as component from "../../components/ui/component";
import * as base from "../../components/ui/base";
import * as modal from "../../components/ui/modal";
import * as paginator from "../../components/ui/paginator";
import * as message from "../../components/ui/message";

// TODO export /////////////////////////////////////////////////////////////////////////////////////////////////////////

export function IdeaPublicPage(): JSX.Element {
  // TODO store ////////////////////////////////////////////////////////////////////////////////////////////////////////

  const ideaReadStore = hook.useSelectorCustom2(slice.idea.ideaReadStore);
  const ideaCommentCreateStore = hook.useSelectorCustom2(
    slice.ideaComment.ideaCommentCreateStore
  );
  const ideaCommentReadListStore = hook.useSelectorCustom2(
    slice.ideaComment.ideaCommentReadListStore
  );
  const ideaRatingReadListStore = hook.useSelectorCustom2(
    slice.ideaRating.ideaRatingReadListStore
  );
  const ideaRatingUpdateStore = hook.useSelectorCustom2(
    slice.ideaRating.ideaRatingUpdateStore
  );

  // TODO hooks ////////////////////////////////////////////////////////////////////////////////////////////////////////

  const dispatch = useDispatch();
  const navigate = useNavigate();
  const id = useParams().id;

  const [
    ideaCommentCreateObject,
    setIdeaCommentCreateObject,
    resetIdeaCommentCreateObject,
  ] = hook.useStateCustom1({
    comment: "",
  });

  const [
    paginationIdeaCommentListObject,
    setPaginationIdeaCommentListObject,
    resetPaginationIdeaCommentListObject,
  ] = hook.useStateCustom1({ page: 1, limit: 5 });

  const [
    isModalPromptNotificationCreateVisible,
    setIsModalPromptNotificationCreateVisible,
  ] = useState(false);
  const [
    modalPromptNotificationCreateForm,
    setModalPromptNotificationCreateForm,
  ] = useState({});

  const [isModalPromptLowRatingVisible, setIsModalPromptLowRatingVisible] =
    useState(false);
  const [modalPromptLowRatingForm, setModalPromptLowRatingForm] = useState({});

  // TODO useEffect ////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    if (!ideaReadStore.data) {
      dispatch(slice.idea.ideaReadStore.action({ idea_id: Number(id) }));
    }
  }, [ideaReadStore.data]);

  useEffect(() => {
    if (!ideaCommentReadListStore.data) {
      dispatch(
        slice.ideaComment.ideaCommentReadListStore.action({
          idea_id: Number(id),
          form: { ...paginationIdeaCommentListObject },
        })
      );
    }
  }, [ideaCommentReadListStore.data]);

  useEffect(() => {
    if (!ideaRatingReadListStore.data) {
      dispatch(
        slice.ideaRating.ideaRatingReadListStore.action({
          idea_id: Number(id),
          form: { limit: -1, page: 1 },
        })
      );
    }
  }, [ideaRatingReadListStore.data]);

  useEffect(() => {
    resetState();
  }, []);

  useEffect(() => {
    resetState();
  }, [id]);

  useEffect(() => {
    if (ideaCommentCreateStore.data || ideaRatingUpdateStore.data) {
      resetState();
    }
  }, [ideaCommentCreateStore.data, ideaRatingUpdateStore.data]);

  useEffect(() => {
    dispatch({
      type: slice.ideaComment.ideaCommentReadListStore.constant.reset,
    });
  }, [paginationIdeaCommentListObject.page]);

  useEffect(() => {
    setPaginationIdeaCommentListObject({
      ...paginationIdeaCommentListObject,
      page: 1,
    });
    dispatch({
      type: slice.ideaComment.ideaCommentReadListStore.constant.reset,
    });
  }, [paginationIdeaCommentListObject.limit]);

  useEffect(() => {
    if (ideaReadStore.data) {
      if (ideaReadStore.data["moderate_status"] !== "??????????????") {
        navigate("/idea/public/list");
      }
    }
  }, [ideaReadStore.data]);

  // TODO functions ////////////////////////////////////////////////////////////////////////////////////////////////////

  function resetState() {
    resetIdeaCommentCreateObject();
    resetPaginationIdeaCommentListObject();
    dispatch({ type: slice.idea.ideaReadStore.constant.reset });
    dispatch({ type: slice.ideaRating.ideaRatingReadListStore.constant.reset });
    dispatch({ type: slice.ideaComment.ideaCommentCreateStore.constant.reset });
    dispatch({
      type: slice.ideaComment.ideaCommentReadListStore.constant.reset,
    });
    dispatch({ type: slice.ideaComment.ideaCommentDeleteStore.constant.reset });
    dispatch({
      type: slice.notification.notificationCreateStore.constant.reset,
    });
  }

  function CreateNotification(form: object) {
    dispatch(
      slice.notification.notificationCreateStore.action({
        form: {
          ...form,
          // @ts-ignore
          description: `${form["description"]}, ??????????????: ${form["answer"]}`,
        },
      })
    );
  }

  function ButtonNotificationIdeaCreate(event: MouseEvent<any>) {
    util.EventMouse1(event, true, true, () => {
      setModalPromptNotificationCreateForm({
        ...modalPromptNotificationCreateForm,
        question: "?????????????? ?????????????? ???????????? ???? ?????????",
        answer: "???????? ??????????????????!",
        name: "???????????? ???? ???????? ?? ?????????? ????????",
        place: "???????? ????????",
        description: `???????????????? ????????: ${ideaReadStore.data["name"]}`,
      });
      setIsModalPromptNotificationCreateVisible(true);
    });
  }

  function ButtonnotificationIdeaCommentCreate(
    event: MouseEvent<any>,
    object: any
  ) {
    util.EventMouse1(event, true, true, () => {
      setModalPromptNotificationCreateForm({
        ...modalPromptNotificationCreateForm,
        question: "?????????????? ?????????????? ???????????? ???? ???????????????????????",
        answer: "?????????????????????? ??????????????!",
        name: "???????????? ???? ?????????????????????? ?? ?????????? ????????",
        place: "???????? ????????",
        description: `???????????????? ????????: ${ideaReadStore.data["name"]} (${
          ideaReadStore.data["author"]["last_name"]
        } ${
          ideaReadStore.data["author"]["first_name"]
        }), ??????????????????????: ${util.GetCleanDateTime(object["created"], true)} (${
          object["author"]["last_name"]
        } ${object["author"]["first_name"]})`,
      });
      setIsModalPromptNotificationCreateVisible(true);
    });
  }

  function CreateComment() {
    dispatch(
      slice.ideaComment.ideaCommentCreateStore.action({
        idea_id: Number(id),
        form: { comment: ideaCommentCreateObject.comment },
      })
    );
  }

  function FormIdeaCommentCreateSubmit(event: FormEvent<HTMLFormElement>) {
    util.EventForm1(event, true, true, () => {
      CreateComment();
    });
  }

  function CreateRating(rating: number) {
    if (rating < 4) {
      setModalPromptLowRatingForm({
        question: "?????????????? ?????????????? ???????????? ?????????????",
        answer: "?????? ???? ?????????????????????? ????????!",
        rating: rating,
      });
      setIsModalPromptLowRatingVisible(true);
    } else {
      dispatch(
        slice.ideaRating.ideaRatingUpdateStore.action({
          idea_id: Number(id),
          form: { rating: rating },
        })
      );
    }
  }

  function CreateLowLevelRating(form: object) {
    dispatch(
      slice.ideaRating.ideaRatingUpdateStore.action({
        idea_id: Number(id),
        // @ts-ignore
        form: { rating: `${form.rating}` },
      })
    );
    dispatch(
      slice.ideaComment.ideaCommentCreateStore.action({
        idea_id: Number(id),
        // @ts-ignore
        form: { comment: `${form.answer}` },
      })
    );
  }

  // TODO return ///////////////////////////////////////////////////////////////////////////////////////////////////////

  return (
    <base.Base1>
      <modal.ModalPrompt1
        isModalVisible={isModalPromptNotificationCreateVisible}
        setIsModalVisible={setIsModalPromptNotificationCreateVisible}
        callback={CreateNotification}
        // @ts-ignore
        form={modalPromptNotificationCreateForm}
      />
      <modal.ModalPrompt1
        isModalVisible={isModalPromptLowRatingVisible}
        setIsModalVisible={setIsModalPromptLowRatingVisible}
        callback={CreateLowLevelRating}
        // @ts-ignore
        form={modalPromptLowRatingForm}
      />
      <component.StatusStore1
        slice={slice.notification.notificationCreateStore}
        consoleLog={constant.DEBUG_CONSTANT}
        showData={true}
        dataText={"???????????? ?????????????? ????????????????????!"}
      />
      <div className="btn-group text-start w-100 m-0 p-0">
        <Link
          to={"/idea/public/list"}
          className="btn btn-sm btn-primary m-1 p-2"
        >
          {"<="} ?????????? ?? ????????????
        </Link>
        {ideaReadStore.data && (
          <button
            type="button"
            className="btn btn-sm btn-outline-danger m-1 p-2 custom-z-index-0"
            onClick={(event) => ButtonNotificationIdeaCreate(event)}
          >
            <i className="fa-solid fa-skull-crossbones m-0 p-1" />
            ???????????? ???? ????????
          </button>
        )}
      </div>
      <component.StatusStore1
        slice={slice.idea.ideaReadStore}
        consoleLog={constant.DEBUG_CONSTANT}
        showData={false}
      />
      {ideaReadStore.data && !ideaReadStore.load && (
        <ul className="row row-cols-1 row-cols-sm-1 row-cols-md-1 row-cols-lg-2 justify-content-center text-center shadow m-0 p-1">
          <div className="card shadow custom-background-transparent-low text-center p-0">
            <div className="card-header bg-warning bg-opacity-10 m-0 p-3">
              <h6 className="lead fw-bold m-0 p-0">
                {ideaReadStore.data["name"]}
              </h6>
            </div>
            <div className="card-body m-0 p-0">
              <div className="m-0 p-0">
                <label className="form-control-sm text-center m-0 p-1">
                  ??????????????????????????:
                  <select
                    className="form-control form-control-sm text-center m-0 p-1"
                    required
                  >
                    <option className="m-0 p-0" value="">
                      {ideaReadStore.data["subdivision"]}
                    </option>
                  </select>
                </label>
                <label className="form-control-sm text-center m-0 p-1">
                  ??????????:
                  <select
                    className="form-control form-control-sm text-center m-0 p-1"
                    required
                  >
                    <option className="m-0 p-0" value="">
                      {ideaReadStore.data["sphere"]}
                    </option>
                  </select>
                </label>
                <label className="form-control-sm text-center m-0 p-1">
                  ??????????????????:
                  <select
                    className="form-control form-control-sm text-center m-0 p-1"
                    required
                  >
                    <option className="m-0 p-0" value="">
                      {ideaReadStore.data["category"]}
                    </option>
                  </select>
                </label>
              </div>
              <div className="m-0 p-0">
                <img
                  src={
                    ideaReadStore.data["image"]
                      ? util.GetStaticFile(ideaReadStore.data["image"])
                      : util.GetStaticFile(
                          "/media/default/idea/default_idea.jpg"
                        )
                  }
                  className="img-fluid img-thumbnail w-75 m-1 p-0"
                  alt="?????????????????????? ??????????????????????"
                />
              </div>
              <div className="m-0 p-0">
                <label className="form-control-sm text-center w-50 m-0 p-1">
                  ?????????? ??????????????????:
                  <input
                    type="text"
                    className="form-control form-control-sm text-center m-0 p-1"
                    defaultValue={ideaReadStore.data["place"]}
                    readOnly={true}
                    placeholder="?????????????? ?????????? ?????????????????? ??????..."
                    required
                    minLength={1}
                    maxLength={300}
                  />
                </label>
              </div>
              <div className="m-0 p-0">
                <label className="form-control-sm text-center w-100 m-0 p-1">
                  ????????????????:
                  <textarea
                    className="form-control form-control-sm text-center m-0 p-1"
                    defaultValue={ideaReadStore.data["description"]}
                    readOnly={true}
                    required
                    placeholder="?????????????? ???????????????? ??????..."
                    minLength={1}
                    maxLength={3000}
                    rows={3}
                  />
                </label>
              </div>
              <div className="m-0 p-0">
                <Link to={`#`} className="btn btn-sm btn-warning m-0 p-2">
                  ??????????: {ideaReadStore.data["author"]["last_name"]}{" "}
                  {ideaReadStore.data["author"]["first_name"]}{" "}
                  {ideaReadStore.data["author"]["position"]}
                </Link>
              </div>
              <div className="d-flex justify-content-between m-1 p-0">
                <label className="text-muted border m-0 p-2">
                  ????????????:{" "}
                  <p className="m-0">
                    {util.GetCleanDateTime(ideaReadStore.data["created"], true)}
                  </p>
                </label>
                <label className="text-muted border m-1 p-2">
                  ????????????????????????????????:{" "}
                  <p className="m-0 p-0">
                    {util.GetCleanDateTime(ideaReadStore.data["updated"], true)}
                  </p>
                </label>
              </div>
            </div>
            <div className="card-footer m-0 p-1">
              <component.StatusStore1
                slice={slice.ideaRating.ideaRatingReadListStore}
                consoleLog={constant.DEBUG_CONSTANT}
                showData={false}
              />
              <component.StatusStore1
                slice={slice.ideaRating.ideaRatingUpdateStore}
                consoleLog={constant.DEBUG_CONSTANT}
                showData={false}
              />
              <div className="d-flex justify-content-between m-0 p-1">
                <span
                  className={
                    ideaReadStore.data["ratings"]["total_rate"] > 7
                      ? "text-success m-0 p-1"
                      : ideaReadStore.data["ratings"]["total_rate"] > 4
                      ? "custom-color-warning-1 m-0 p-1"
                      : "text-danger m-0 p-1"
                  }
                >
                  ??????????????
                </span>
                <Navbar className="text-center m-0 p-0">
                  <div className="m-0 p-0">
                    <small>?????????????? / ????????????</small>
                  </div>
                  <Container className="m-0 p-0">
                    <Nav className="me-auto dropdown m-0 p-0">
                      <NavDropdown
                        title={
                          util.GetSliceString(
                            ideaReadStore.data["ratings"]["total_rate"],
                            3,
                            false
                          ) +
                          " /  " +
                          ideaReadStore.data["ratings"]["count"]
                        }
                        className={
                          ideaReadStore.data["ratings"]["total_rate"] > 7
                            ? ideaReadStore.data["ratings"]["count"] > 0
                              ? "btn btn-sm bg-success bg-opacity-50 badge rounded-pill"
                              : "btn btn-sm bg-success bg-opacity-50 badge rounded-pill disabled"
                            : ideaReadStore.data["ratings"]["total_rate"] > 4
                            ? ideaReadStore.data["ratings"]["count"] > 0
                              ? "btn btn-sm bg-warning bg-opacity-50 badge rounded-pill"
                              : "btn btn-sm bg-warning bg-opacity-50 badge rounded-pill disabled"
                            : ideaReadStore.data["ratings"]["count"] > 0
                            ? "btn btn-sm bg-danger bg-opacity-50 badge rounded-pill"
                            : "btn btn-sm bg-danger bg-opacity-50 badge rounded-pill disabled"
                        }
                      >
                        <ul className="m-0 p-0">
                          <component.StatusStore1
                            slice={slice.ideaRating.ideaRatingReadListStore}
                            consoleLog={constant.DEBUG_CONSTANT}
                            showData={false}
                          />
                          {ideaRatingReadListStore.data &&
                            ideaRatingReadListStore.data.list.map(
                              // @ts-ignore
                              (rate, index) => (
                                <li
                                  key={index}
                                  className={
                                    rate["rating"] > 7
                                      ? "list-group-item bg-success bg-opacity-10"
                                      : rate["rating"] > 4
                                      ? "list-group-item bg-warning bg-opacity-10"
                                      : "list-group-item bg-danger bg-opacity-10"
                                  }
                                >
                                  <small className="">
                                    {`${rate["author"]["last_name"]} 
                                    ${rate["author"]["first_name"]} : 
                                    ${rate["rating"]}`}
                                  </small>
                                </li>
                              )
                            )}
                        </ul>
                      </NavDropdown>
                    </Nav>
                  </Container>
                </Navbar>
                {ideaRatingReadListStore.data && (
                  <span className="m-0 p-1">
                    <div className="m-0 p-0">
                      ?????????????? ???? ???????? ???? 10 ?????????? ?????? ???????????? ????????:
                    </div>
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 1
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 0.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(1)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 2
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 1.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(2)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 3
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 2.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(3)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 4
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 3.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(4)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 5
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 4.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(5)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 6
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 5.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(6)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 7
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 6.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(7)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 8
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 7.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(8)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 9
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 8.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(9)}
                    />
                    <i
                      style={{
                        color:
                          ideaRatingReadListStore.data["self_rate"] > 7
                            ? "#00ff00"
                            : ideaRatingReadListStore.data["self_rate"] > 4
                            ? "#ffaa00"
                            : "#ff0000",
                      }}
                      className={
                        ideaRatingReadListStore.data["self_rate"] >= 10
                          ? "btn fas fa-star m-0 p-0"
                          : ideaRatingReadListStore.data["self_rate"] >= 9.5
                          ? "btn fas fa-star-half-alt m-0 p-0"
                          : "btn far fa-star m-0 p-0"
                      }
                      onClick={() => CreateRating(10)}
                    />
                    <div className="m-0 p-0">???????? ????????????</div>
                  </span>
                )}
              </div>
              <div className="d-flex justify-content-between m-0 p-1">
                <span className="text-secondary m-0 p-1">??????????????????????</span>
                <i className="fa-solid fa-comment m-0 p-1">
                  {" "}
                  {ideaReadStore.data["comments"]["count"]}
                </i>
              </div>
            </div>
            <div className="card-footer m-0 p-0">
              <component.StatusStore1
                slice={slice.ideaComment.ideaCommentCreateStore}
                consoleLog={constant.DEBUG_CONSTANT}
                showData={false}
              />
              <div className="card m-0 p-2">
                <div className="order-md-last m-0 p-0">
                  <div className="m-0 p-0 my-2">
                    <form
                      className="card"
                      onSubmit={(event) => {
                        FormIdeaCommentCreateSubmit(event);
                      }}
                    >
                      <div className="input-group">
                        <input
                          type="text"
                          className="form-control form-control-sm text-center m-0 p-1"
                          value={ideaCommentCreateObject.comment}
                          required
                          placeholder="?????????????? ?????????????????????? ??????..."
                          minLength={1}
                          maxLength={300}
                          onChange={(e) =>
                            setIdeaCommentCreateObject({
                              ...ideaCommentCreateObject,
                              comment: e.target.value.replace(
                                util.RegularExpression.GetRegexType({
                                  numbers: true,
                                  cyrillic: true,
                                  space: true,
                                  punctuationMarks: true,
                                }),
                                ""
                              ),
                            })
                          }
                        />
                        <button
                          type="submit"
                          className="btn btn-secondary custom-z-index-0"
                        >
                          <i className="fa-solid fa-circle-check m-0 p-1" />
                          ??????????????????
                        </button>
                      </div>
                    </form>
                  </div>
                  <div className="card m-0 p-2">
                    <div className="order-md-last m-0 p-0">
                      {!ideaCommentReadListStore.load &&
                      ideaCommentReadListStore.data ? (
                        ideaCommentReadListStore.data.list.length > 0 ? (
                          <ul className="list-group m-0 p-0">
                            <label className="form-control-sm text-center m-0 p-1">
                              ???????????????????? ???????????????????????? ???? ????????????????:
                              <select
                                className="form-control form-control-sm text-center m-0 p-1"
                                value={paginationIdeaCommentListObject.limit}
                                onChange={(event) =>
                                  setPaginationIdeaCommentListObject({
                                    ...paginationIdeaCommentListObject,
                                    // @ts-ignore
                                    limit: event.target.value,
                                  })
                                }
                              >
                                <option disabled defaultValue={""} value="">
                                  ???????????????????? ???? ????????????????
                                </option>
                                <option value="5">5</option>
                                <option value="10">10</option>
                                <option value="30">30</option>
                                <option value="-1">??????</option>
                              </select>
                            </label>
                            {!ideaCommentReadListStore.load &&
                              ideaCommentReadListStore.data && (
                                <paginator.Pagination1
                                  totalObjects={
                                    ideaCommentReadListStore.data[
                                      "x-total-count"
                                    ]
                                  }
                                  limit={paginationIdeaCommentListObject.limit}
                                  page={paginationIdeaCommentListObject.page}
                                  // @ts-ignore
                                  changePage={(page) =>
                                    setPaginationIdeaCommentListObject({
                                      ...paginationIdeaCommentListObject,
                                      page: page,
                                    })
                                  }
                                />
                              )}
                            {!ideaCommentReadListStore.load &&
                              ideaCommentReadListStore.data &&
                              ideaCommentReadListStore.data.list.map(
                                // @ts-ignore
                                (object, index) => (
                                  <li
                                    className="list-group-item m-0 p-1"
                                    key={index}
                                  >
                                    <div className="d-flex justify-content-between m-0 p-0">
                                      <h6 className="btn btn-sm btn-outline-warning m-0 p-2">
                                        {object["author"]["last_name"]}{" "}
                                        {object["author"]["first_name"]}
                                      </h6>
                                      <span className="text-muted m-0 p-0">
                                        {util.GetCleanDateTime(
                                          object["created"],
                                          true
                                        )}
                                        <button
                                          type="button"
                                          className="btn btn-sm btn-outline-danger m-1 p-0"
                                          onClick={(event) =>
                                            ButtonnotificationIdeaCommentCreate(
                                              event,
                                              object
                                            )
                                          }
                                        >
                                          <i className="fa-solid fa-skull-crossbones m-0 p-1" />
                                          ???????????? ???? ??????????????????????
                                        </button>
                                      </span>
                                    </div>
                                    <div className="d-flex justify-content-center m-0 p-1">
                                      <small className="text-muted m-0 p-1">
                                        {object["comment"]}
                                      </small>
                                    </div>
                                  </li>
                                )
                              )}
                            {!ideaCommentReadListStore.load &&
                              ideaCommentReadListStore.data && (
                                <paginator.Pagination1
                                  totalObjects={
                                    ideaCommentReadListStore.data[
                                      "x-total-count"
                                    ]
                                  }
                                  limit={paginationIdeaCommentListObject.limit}
                                  page={paginationIdeaCommentListObject.page}
                                  // @ts-ignore
                                  changePage={(page) =>
                                    setPaginationIdeaCommentListObject({
                                      ...paginationIdeaCommentListObject,
                                      page: page,
                                    })
                                  }
                                />
                              )}
                          </ul>
                        ) : (
                          <message.Message.Secondary>
                            ?????????????????????? ???? ??????????????!
                          </message.Message.Secondary>
                        )
                      ) : (
                        ""
                      )}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </ul>
      )}
    </base.Base1>
  );
}
